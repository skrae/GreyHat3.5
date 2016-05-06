##Seitz, J. (2008). Grey Hat Python: Python programming for hackers and reverse engineers. San Francisco, CA: No Starch Press. 
##Chapter 1 page 8
##Rewritten for Python 3.5 by Justin Brenneman

from ctypes import *

libc = CDLL("libc.so.6")
message_string = b"Hello world!\n"
libc.printf(b"Testing:  %s", message_string)
