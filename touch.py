from pathlib import Path
import sys

print
if len(sys.argv) > 2:
	for x in range(1, len(sys.argv)):
		Path(sys.argv[x]).touch()

elif len(sys.argv) == 2:
	Path(sys.argv[1]).touch()

else:
	print("Touch v1 - JFC Coding")
	print("How to: touch <filename>.<extention>")
	print("You can add as many file names to create more files as you would like")