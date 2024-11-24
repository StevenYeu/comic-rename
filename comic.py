import re
from os import listdir, rename
from os.path import isfile, join
import argparse

parser = argparse.ArgumentParser(
    prog="Comic Rename",
    description="Rename comics files to 'Name Vol Num' format",
)
parser.add_argument("src")
parser.add_argument("-d", "--dry", action="store_true")
args = parser.parse_args()
directory_path: str = args.src
is_dry_run: bool = args.dry

patternSpaceParen = r"(\s*)\((.*?)\)(\s*)"
regexSpaceParen = re.compile(patternSpaceParen)

patternVol = r"(v.+)(\d+)"
regexVol = re.compile(patternVol)

patternVolNum = r"(?!v)(\d+)"
regexVolNum = re.compile(patternVolNum)

onlyfiles = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
for f in onlyfiles:
    if not f.endswith(".cbr") and not f.endswith(".cbz"):
        continue
    originalFile = join(directory_path, f)
    newName = regexSpaceParen.sub("", f)
    matchList = regexVolNum.findall(newName)
    if len(matchList) == 0:
        continue
    volNum = matchList[-1]
    replacement = "Vol. " + volNum
    finalName = regexVol.sub(replacement, newName)
    newFile = join(directory_path, finalName)
    if not is_dry_run:
        print(f"Renaming {f} to {finalName}")
        try:
            rename(originalFile, newFile)
        except FileNotFoundError:
            print(f"Can't find {f}")
    else:
        print("DRY RUN")
        print(f"Renaming {f} to {finalName}")
        print("END OF DRY RUN")
