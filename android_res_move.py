# Created by ahsanzaheer on 27.02.18.
# <ahsan024@gmail.com, ahsan.zaheer@hotmail.com>

import sys
import os
import os.path
import shutil

def checkArgs():
  argLen = len(sys.argv)
  if argLen < 4:
      raise StandardError("Please enter missing arguments")
  
  return True

def sanityCheck():
    source = sys.argv[1]
    dest = sys.argv[2]
    filename = sys.argv[3]

    if not os.path.isdir(source):
      raise IOError('Source path does not exist')

    if not os.path.isdir(dest):
      raise IOError('Destination path does not exist')

    print "---------------------------------------------"
    copyFiles(source, dest, filename)


def copyFiles(source, dest, filename):
  for root, dirs, files in os.walk(source, topdown=False):
    for name in files:
      if (name == filename):
        file_path = root + '/' + filename
        path = os.path.dirname(file_path)
        base = os.path.basename(path)
        print "Source path " +file_path

        dest_sub_dir = dest + '/' + base
        
        if not os.path.exists(dest_sub_dir):
          os.mkdir(dest_sub_dir)
          
        shutil.copy(file_path, dest_sub_dir)




if (checkArgs()):
    sanityCheck()


