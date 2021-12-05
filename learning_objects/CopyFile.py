import re
import glob
import shutil as s
files=list(glob.iglob("./Exercises/Exercises WeGoSTEM/*_Meta", recursive=True))
print(files)


# for directory in files:
#     print(directory)
#     s.copytree(directory, f"{directory}F")


files=list(glob.iglob("./Exercises/Exercises WeGoSTEM/*_MetaF/metadata.md", recursive=True))

for file in files:
	print(file)

for file in files:
	with open (file, "r+") as f:
		text=f.read()
		text=re.sub("language: nl", "language: fr", text)
		f.seek(0)
		f.write(text)
		f.truncate()

