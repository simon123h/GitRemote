from __future__ import print_function


import msvcrt

while True:
    k = msvcrt.getch()
    print "pressed:", k, ord(k)
