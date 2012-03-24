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
import array
from nox.lib.packet.ethernet import *
from nox.netapps.tests import unittest
from nox.coreapps.testharness.testdefs import *


ether_eapol = \
"""\
\x01\x80\xc2\x00\x00\x03\x50\x54\x00\x00\x00\x01\x88\x8e\x02\x02\
\x00\x00\
"""

def testEAPOL():
    eth = ethernet(ether_eapol)
    nox_test_assert(eth.tostring() == ether_eapol, "eapol")
