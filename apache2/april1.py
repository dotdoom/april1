#!/usr/bin/env python2.7
# coding: utf-8

import random
import sys
import time

random.seed()

page = list(sys.stdin.read().decode('utf-8'))

if random.randint(0, 10) > 6:
    for i in xrange(0, len(page)):
        c = page[i].lower()
        if c >= u'а' and c <= u'я':
            if i % 2:
                c = c.upper()
            else:
                c = c.lower()
            page[i] = c

sys.stdout.write(''.join(page).encode('utf-8'))
