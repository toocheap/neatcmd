#!/usr/bin/env python
# encoding:utf-8

import time, os, sys
def main(cmd, inc=60):
    while True:
        os.system(cmd)
        time.sleep(inc)

if __name__ == '__main__':
    numargs = len(sys.argv) -1
    if numargs < 1 or numargs > 2:
        print "usage: " + sys.argv[0] + " command [seconds delay]"
        sys.exit(1)
    cmd = sys.argv[1]
    if numargs < 2:
        main(cmd)
    else:
        inc = int(sys.argv[2])
        main(cmd, inc)

