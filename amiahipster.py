#!/usr/bin/env python

USAGE = '''
Python script to determine if you are a hipster
when writing JavaScript

usage:
	amiahipster.py path/to/mycode.js
'''

import sys

try:
	file_name = sys.argv[1]
except IndexError:
	print USAGE
	sys.exit(0)

f = open(file_name)

lines = [line.replace('\n', '') for line in f.readlines()]
lines = [line for line in lines if line]

semis = filter(lambda line: ';' in line, lines)

if file_name.endswith('.coffee') or len(semis) < len(lines) / 10:
	print "Yeah, you're probably a hipster."
else:
	print "Nope, you're probably not a hipster."
