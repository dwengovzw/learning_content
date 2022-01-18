import re
import glob

files=list(glob.iglob("**/*_I_*/index.md", recursive=True))

for ff in files:
	with open (ff, "r+") as fin:
		text=fin.read()
		#skos1="Test"
		#skos2=re.escape('http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen')
	#	print(skos2)	
		text=re.sub("\", "", text)
		fin.seek(0)
		fin.write(text)
		fin.truncate()

print('\n' .join(map(str, files)))

    # 'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    # 'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'

#	'http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen'