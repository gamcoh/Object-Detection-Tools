import os

XML_DIR = os.path.join(
	os.path.dirname(__file__),
	'annotations/xmls'
)

for filename in os.listdir(XML_DIR):
	if not filename.endswith('.xml'):
		continue

	file = os.path.join(XML_DIR, filename)

	with open(file, 'r') as f:
		if '<object>' not in f.read():
			print("INFO: file: %s dosen't have object in his content, removing file." % file)
			os.remove(file)
