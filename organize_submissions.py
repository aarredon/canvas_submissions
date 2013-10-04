#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

# {0} source
# {1} destination
COPY = "cp '{0}' '{1}'"

SUBMISSIONS = 'submissions.zip'
print "Decompressing %s" % SUBMISSIONS 
result = subprocess.call(['unzip',SUBMISSIONS])

if result == 0:
  print "decompressing successful"
  files = [f for f in os.listdir('.') if os.path.isfile(f) and f != '%s'%(SUBMISSIONS)]
  MYCWD = os.getcwd()
  for i in files:
    name = i.split('_')
    NEWDIR = ''
    simple = True
    unknown_format = False 
    
    if len(name) > 1:
      simple = True
    else:
      unknown_format = True 
    
    if not unknown_format:
      # last_first
      if simple:
        NEWDIR = name[0] 
        try:
          os.mkdir('{0}'.format(os.path.join(MYCWD,NEWDIR)))
        except OSError as e:
          pass

      if NEWDIR:
        # copy the file to the new/existing directory
        print "  " + COPY.format(i,NEWDIR)
        os.system(COPY.format(i,NEWDIR))
    else:
      print "Unknown format"

  # cleanup the extracted files
  for i in files:
    os.remove(i)

  print "organization complete"

else:
  print "decompressing failed"

