from os import listdir, rename
from os.path import isfile, join
import sys
import re

mypath = sys.argv[1]

patternSpaceParen = "(\s*)\((.*?)\)(\s*)"
regexSpaceParen = re.compile(patternSpaceParen)

patternVol = "(v.+)(\d+)"
regexVol = re.compile(patternVol)

patternVolNum = "(?!v)(\d+)"
regexVolNum = re.compile(patternVolNum)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
  originalFile = join(mypath, f)
  newName = regexSpaceParen.sub("", f)
  volNum = regexVolNum.search(f)
  replacement = "Vol. " + volNum.group(0)
  finalNName = regexVol.sub(replacement, newName)
  newFile = join(mypath, finalNName)
  rename(originalFile, newFile)
