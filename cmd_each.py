#!/usr/bin/env python
# vim:fenc=utf8
"""
Run each line as parameter for a command line.

-- parameter file --
aaa bbb ccc
ddd eee fff
ggg hhh iii
[EOF

% cmd_each parameter_file "echo $1 $2 $3"
# This runs:
echo aaa bbb ccc
echo ddd eee fff
echo ggg hhh iii
"""
import os, sys, re, string

def perf_cmd(cmd, args):
    pat = re.compile(r"%(\d)")
    pats = pat.findall(cmd)
    for p in pats:
        r = '%' + p
        i= int(p)-1
        cmd = string.replace(cmd, r, args[i])
    os.system(cmd)

def main(pfile, cmd):
    with open(pfile, "r") as pf:
        lines = pf.readlines()
        for l in lines:
            perf_cmd(cmd, l.split())

if __name__ == '__main__':
    numargs = len(sys.argv) -1
    if numargs != 2:
        print "usage: " + sys.argv[0] + " parameter_file command "
        sys.exit(1)
    pfile = sys.argv[1]
    cmd = sys.argv[2]
    main(pfile, cmd)

