import re
import glob
files=list(glob.iglob("**/*.md", recursive=True))
print(files)
ffiles=[str for str in files if any(substring in str for substring in ["_Meta"])]
print(ffiles)
for ff in ffiles:
	with open (ff, "r+") as fin:
		text=fin.read()
		text=re.sub("language: nl", "language: fr", text)
		fin.seek(0)
		fin.write(text)
		fin.truncate()	