# Copyright 2008 (C) Nicira, Inc.
# 
# This file is part of NOX.
# 
# NOX is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# NOX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with NOX.  If not, see <http://www.gnu.org/licenses/>.

from nox.lib.core     import Component
from nox.lib.netinet.netinet import *
from nox.netapps.bindings_storage.pybindings_storage import pybindings_storage, Name
from nox.netapps.tests import unittest
from twisted.internet.defer import Deferred
from nox.netapps.storage import Storage
import time

pyunit = __import__('unittest')

class BSLocationTestCase(unittest.NoxTestCase):
    """ Bindings_Storage python tests for Location/Switch functionality"""

    def configure(self,configuration):
      pass

    def install(self):
      self.bs = self.resolve(pybindings_storage) 
      self.store = self.resolve(Storage)
      #self.debug = True
      self.debug = False

    def getInterface(self):
        return str(BSLocationTestCase)
      
    def check_wait(self): 
      self.wait_count = self.wait_count - 1
      if self.wait_count == 0: 
        self.next_fn() 

    def names_cb(self, names):
      if(self.debug): 
        print "expected names: " 
        for n in self.expected_names: 
          print str(n) 
        print "got names: " 
        for n in names: 
          print str(n) 
      
      assert(len(names) == len(self.expected_names))

      for n in names: 
        found = False
        for e in self.expected_names:
          if e == n: 
            found = True
            break
        assert(found)

      self.check_wait() 


    def clear_cb(self):
        self.num_triggers_inserted = 0 
        d = self.store.put_table_trigger("bindings_location", True, 
                                            self.trigger_callback)
        d.addCallback(self.trigger_inserted_callback)  
      
    def trigger_inserted_callback(self, res): 
      result , tid = res 

      if (result[0] != 0): 
        print "put trigger failed: " + str(result[1]) 
        self.exit_test(False) 
        return 
      self.tid = tid  
      self.run_test1() 

    def trigger_callback(self, trigger_id, row, reason):
      self.check_wait() 

    def run_test1(self):
      
      dpid = datapathid.from_host(1)
      port = 1
      
      if(self.debug): print "adding location (1,1) as office-5 " 
      self.bs.add_name_for_location(dpid,port,"office-5", Name.LOCATION) 
      
      i = 1 << 47 # should be a LONG
      if(self.debug): print "adding switch (" + str(i) + ") as of6k " 
      self.bs.add_name_for_location(datapathid.from_host(i),
                                    0,"of6k", Name.SWITCH) 
      
      self.wait_count = 2
      self.next_fn = self.run_test2
    
    def run_test2(self): 
      if(self.debug): print "getting name for location 1,1" 
      dpid = datapathid.from_host(1)
      port = 1
      self.expected_names = [ ("office-5", Name.LOCATION), ]

      self.bs.get_names_for_location(dpid,port,Name.LOCATION,self.names_cb)

      self.next_fn = self.run_test3
      self.wait_count = 1

    def run_test3(self):

      i = 1 << 47 # should be a LONG
      if(self.debug): print "getting name for switch " + str(i)  
      self.expected_names = [ ("of6k", Name.SWITCH), ]
      self.bs.get_names_for_location(datapathid.from_host(i),0,
                                    Name.SWITCH,self.names_cb) 

      self.next_fn = self.run_test4
      self.wait_count = 1

    def run_test4(self): 
      i = (1 << 47) # should be a LONG
      if(self.debug): print "removing switch " + str(i)  
      self.bs.remove_name_for_location(datapathid.from_host(i),0,
                                    "", Name.SWITCH) 

      self.next_fn = self.run_test5
      self.wait_count = 1

    def run_test5(self):
      i = (1 << 47) # should be a LONG
      if(self.debug): print "getting name for nonexistent switch "
      self.expected_names = [ ]
      self.bs.get_names_for_location(datapathid.from_host(i),0,
                                    Name.SWITCH,self.names_cb) 

      self.next_fn = self.run_test6
      self.wait_count = 1
    
    def run_test6(self): 
      i = (1 << 47) # should be a LONG
      if(self.debug): print "removing location (1,1)"
      self.bs.remove_name_for_location(datapathid.from_host(1),1,
                                    "office-5", Name.LOCATION) 

      self.next_fn = self.run_test7
      self.wait_count = 1

    def run_test7(self):
    
      if(self.debug): print "getting name for location after remove"
      self.expected_names = [ ("none;000000000001:1",1), ] # should get dpid:port
      self.bs.get_names_for_location(datapathid.from_host(1),1,
                                    Name.LOCATION,self.names_cb) 

      self.next_fn = self.tear_down
      self.wait_count = 1

 

    def tear_down(self): 
      d = self.store.remove_trigger(self.tid)
      d.addCallback(self.remove_trigger_callback)
    
    def start(self): 
      self.bs.clear(self.clear_cb) 

      self.deferred = Deferred()
      return self.deferred

    def exit_test(self, success) : 
      if(not success):
        assert(False)
      self.deferred.callback("done") # tell test-suite that we are done
    
    def remove_trigger_callback(self, result): 
      if (result[0] != 0): 
        print "remove trigger failed: " + str(result[1]) 
        self.exit_test(False) 
        return 
      
      self.exit_test(True) # success 


def suite(ctxt):
    suite = pyunit.TestSuite()
    suite.addTest(BSLocationTestCase("start", ctxt))
    return suite
