import re
import glob

files=list(glob.iglob("**/*_I_*/index.md", recursive=True))

for ff in files:
	with open (ff, "r+") as fin:
		text=fin.read()
		skos1=re.escape("http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', \n    'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso")
		skos2=re.escape('http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen')		
		text=re.sub(skos1, skos2, text)
		fin.seek(0)
		fin.write(text)
		fin.truncate()

print('\n' .join(map(str, files)))

    # 'http://ilearn.ilabt.imec.be/vocab/curr1/c-andere-talen', 
    # 'http://ilearn.ilabt.imec.be/vocab/ondniv/sec-gr2-doorstroom-aso'

#	'http://ilearn.ilabt.imec.be/vocab/curr1/s-digitale-media-en-toepassingen'