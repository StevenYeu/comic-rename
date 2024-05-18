import re
import sys
from os import listdir, rename
from os.path import isfile, join

mypath = sys.argv[1]

patternSpaceParen = r"(\s*)\((.*?)\)(\s*)"
regexSpaceParen = re.compile(patternSpaceParen)

patternVol = r"(v.+)(\d+)"
regexVol = re.compile(patternVol)

patternVolNum = r"(?!v)(\d+)"
regexVolNum = re.compile(patternVolNum)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
    originalFile = join(mypath, f)
    newName = regexSpaceParen.sub("", f)
    volNum = regexVolNum.search(f)
    replacement = "Vol. " + volNum.group(0)
    finalName = regexVol.sub(replacement, newName)
    newFile = join(mypath, finalName)
    print(f"Renaming {f} to {finalName}")
    try:
        rename(originalFile, newFile)
    except FileNotFoundError:
        print(f"Can't find {f}")
