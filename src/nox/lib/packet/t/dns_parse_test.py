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

from nox.lib.packet.dns import *

from nox.coreapps.testharness.testdefs import *

# Copied from curses so you don't have to import
# another package which is not standard on some
# Linux distros
def _ctoi(c):
    if type(c) == type(""):
        return ord(c)
    else:
        return c
def isascii(c): return _ctoi(c) <= 127   


dns_test_1 = "\xa1\xdb\x81\x80\x00\x01\x00\x02\x00\x09\x00\x04\x05\x66\x61\x72\x6d\x33\x06\x73\x74\x61\x74\x69\x63\x06\x66\x6c\x69\x63\x6b\x72\x03\x63\x6f\x6d\x00\x00\x01\x00\x01\xc0\x0c\x00\x05\x00\x01\x00\x00\x01\x2c\x00\x27\x05\x66\x61\x72\x6d\x33\x06\x73\x74\x61\x74\x69\x63\x06\x66\x6c\x69\x63\x6b\x72\x06\x79\x61\x68\x6f\x6f\x33\x06\x61\x6b\x61\x64\x6e\x73\x03\x6e\x65\x74\x00\xc0\x35\x00\x01\x00\x01\x00\x00\x01\x2c\x00\x04\x45\x93\x5a\x9e\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x08\x05\x61\x73\x69\x61\x39\xc0\x50\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x0f\x02\x7a\x61\x06\x61\x6b\x61\x64\x6e\x73\x03\x6f\x72\x67\x00\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x05\x02\x7a\x64\xc0\x8f\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x05\x02\x7a\x62\xc0\x8f\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x07\x04\x65\x75\x72\x31\xc0\x50\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x07\x04\x75\x73\x65\x33\xc0\x50\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x07\x04\x75\x73\x77\x32\xc0\x50\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x05\x02\x7a\x63\xc0\x8f\xc0\x50\x00\x02\x00\x01\x00\x02\x85\xba\x00\x07\x04\x75\x73\x65\x34\xc0\x50\xc0\x8c\x00\x01\x00\x01\x00\x02\x85\xbb\x00\x04\xc3\xdb\x03\xa9\xc0\xb8\x00\x01\x00\x01\x00\x02\x85\xbb\x00\x04\xce\x84\x64\x69\xc1\x02\x00\x01\x00\x01\x00\x02\x85\xbb\x00\x04\x7c\xd3\x28\x04\xc0\xa7\x00\x01\x00\x01\x00\x02\x85\xbb\x00\x04\x3f\xd1\x03\x84"

dns_test_2 = "\xb8\xc1\x81\x80\x00\x01\x00\x08\x00\x09\x00\x04\x05\x70\x69\x78\x65\x6c\x0a\x71\x75\x61\x6e\x74\x73\x65\x72\x76\x65\x03\x63\x6f\x6d\x00\x00\x01\x00\x01\xc0\x0c\x00\x05\x00\x01\x00\x01\x50\x54\x00\x1f\x03\x67\x65\x6f\x0a\x71\x75\x61\x6e\x74\x73\x65\x72\x76\x65\x03\x63\x6f\x6d\x06\x61\x6b\x61\x64\x6e\x73\x03\x6e\x65\x74\x00\xc0\x32\x00\x01\x00\x01\x00\x00\x00\x78\x00\x04\x04\x4e\xf3\x26\xc0\x32\x00\x01\x00\x01\x00\x00\x00\x78\x00\x04\x04\x4e\xf3\x24\xc0\x32\x00\x01\x00\x01\x00\x00\x00\x78\x00\x04\x04\x4e\xf3\x22\xc0\x32\x00\x01\x00\x01\x00\x00\x00\x78\x00\x04\x04\x4e\xf3\x20\xc0\x32\x00\x01\x00\x01\x00\x00\x00\x78\x00\x04\x04\x4e\xf3\x23\xc0\x32\x00\x01\x00\x01\x00\x00\x00\x78\x00\x04\x04\x4e\xf3\x21\xc0\x32\x00\x01\x00\x01\x00\x00\x00\x78\x00\x04\x04\x4e\xf3\x25\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x07\x04\x75\x73\x77\x32\xc0\x45\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x07\x04\x75\x73\x65\x33\xc0\x45\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x0f\x02\x7a\x62\x06\x61\x6b\x61\x64\x6e\x73\x03\x6f\x72\x67\x00\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x05\x02\x7a\x61\xc0\xf6\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x05\x02\x7a\x63\xc0\xf6\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x05\x02\x7a\x64\xc0\xf6\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x08\x05\x61\x73\x69\x61\x39\xc0\x45\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x07\x04\x75\x73\x65\x34\xc0\x45\xc0\x45\x00\x02\x00\x01\x00\x01\x8f\xe9\x00\x07\x04\x65\x75\x72\x31\xc0\x45\xc1\x0e\x00\x01\x00\x01\x00\x01\x8f\xea\x00\x04\xc3\xdb\x03\xa9\xc0\xf3\x00\x01\x00\x01\x00\x01\x8f\xea\x00\x04\xce\x84\x64\x69\xc1\x1f\x00\x01\x00\x01\x00\x01\x8f\xea\x00\x04\x7c\xd3\x28\x04\xc1\x30\x00\x01\x00\x01\x00\x01\x8f\xea\x00\x04\x3f\xd1\x03\x84"

def check_string_for_nonascii(checkme):
    for char in checkme:
        if not isascii(char):
            nox_test_assert(0, 'Not ASCII')

def check_name(list):
    for item in list:
        check_string_for_nonascii(item.name)

def test_dns_2():
    """test complex dns packet"""
    d = dns(dns_test_2)
    assert(d)
    nox_test_assert(len(d.questions)   == 1, 'Questions')
    nox_test_assert(len(d.answers)     == 8, 'Answers')
    nox_test_assert(len(d.authorities) == 9, 'Authorities')
    nox_test_assert(len(d.additional)  == 4, 'Additional')
    check_name(d.questions)
    check_name(d.answers)
    check_name(d.authorities)
    check_name(d.additional)

def test_dns_1():
    """test complex dns packet"""
    d = dns(dns_test_1)
    assert(d)
    nox_test_assert(len(d.questions)   == 1, 'Questions')
    nox_test_assert(len(d.answers)     == 2, 'Answers')
    nox_test_assert(len(d.authorities) == 9, 'Authorities')
    nox_test_assert(len(d.additional)  == 4, 'Additional')

    check_name(d.questions)
    check_name(d.answers)
    check_name(d.authorities)
    check_name(d.additional)
