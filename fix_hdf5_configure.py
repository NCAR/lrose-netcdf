#!/usr/bin/env python

#===========================================================================
#
# Fix the configure script for HDF5 library
# This replaces the definition of OLD_HEADER_FILENAME with
# XXX_XXXXXX_XXXXXXXX so that it is no longer active in the build
#
#===========================================================================

from __future__ import print_function
import os
import sys
import shutil
import subprocess
from optparse import OptionParser
import time
from datetime import datetime
from datetime import date
from datetime import timedelta
import glob

def main():

    # globals

    global thisScriptName
    thisScriptName = os.path.basename(__file__)
    
    # parse the command line

    global options
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option('--debug',
                      dest='debug', default=True,
                      action="store_true",
                      help='Set debugging on')
    parser.add_option('--configurePathOrig',
                      dest='configurePathOrig', default="configure",
                      help='Path to original configure script')
    parser.add_option('--configurePathNew',
                      dest='configurePathNew', default="configure.new",
                      help='Path to new configure script')

    (options, args) = parser.parse_args()
    
    if (options.debug):
        print("Running %s:" % thisScriptName, file=sys.stderr)
        print("  configurePathOrig: ", options.configurePathOrig, file=sys.stderr)
        print("  configurePathNew: ", options.configurePathNew, file=sys.stderr)

    # read in original configure
        
    fp = open(options.configurePathOrig, 'r')
    lines = fp.readlines()
    fp.close()

    if (options.debug):
        print("Read in orig file: ", options.configurePathOrig, file=sys.stderr)

    # replace OLD_HEADER_FILENAME string whereever it appears

    newLines = []
    for line in lines:
        newLine = line.replace("OLD_HEADER_FILENAME", "XXX_XXXXXX_XXXXXXXX")
        newLines.append(newLine)

    # write the new file

    new = open(options.configurePathNew, "w")
    for newLine in newLines:
        new.write(newLine)
    new.close()
    shellCmd("chmod +x " +  options.configurePathNew)
    if (options.debug):
        print("Wrote new file: ", options.configurePathNew, file=sys.stderr)
    
    sys.exit(0)

########################################################################
# Run a command in a shell, wait for it to complete

def shellCmd(cmd):

    print("Running cmd:", cmd, file=sys.stderr)
    
    try:
        retcode = subprocess.check_call(cmd, shell=True)
        if retcode != 0:
            print("Child exited with code: ", retcode, file=sys.stderr)
            sys.exit(1)
        else:
            if (options.debug):
                print("Child returned code: ", retcode, file=sys.stderr)
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)
        sys.exit(1)

    print("    done", file=sys.stderr)
    
########################################################################
# Run - entry point

if __name__ == "__main__":
   main()
