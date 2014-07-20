#!/usr/bin/env python

import random
import string  
import os


random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])

print random