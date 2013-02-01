#!/usr/bin/env python

'''
Python script to determine if you are a hipster
when writing JavaScript

usage:
	amiahipster.py path/to/mycode.js
'''

import sys

f = open(sys.argv[1])

lines = [line.replace('\n', '') for line in f.readlines()]
lines = [line for line in lines if line]

semis = filter(lambda line: ';' in line, lines)

if len(semis) < len(lines) / 10:
	print "Yeah, you're probably a hispter."
else:
	print "Nope, you're probably not a hipster."
