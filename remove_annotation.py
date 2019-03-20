import os
import argparse

import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Give me a label')
parser.add_argument('-n', '--name', type=str, help='The name of the annotation you want to remove in every xml file', dest="annotation_name", required=True)
args = parser.parse_args()

XML_DIR = os.path.join(
	os.path.dirname(__file__),
	'annotations/xmls' # -> change to your xml dir
)

for xml_file in os.listdir(XML_DIR):
	print(xml_file)

	if not xml_file.endswith('.xml'):
		continue
	
	file = os.path.join(XML_DIR, xml_file)
	tree = ET.parse(file)
	root = tree.getroot()
	if root.tag != 'annotation':
		raise Exception(
			'pascal voc xml root element should be annotation, rather than {}'.format(root.tag))
	
	xmlEdited = False

	for obj in [elem for elem in root.iter() if elem.tag == 'object']:
		labelName = obj.find('name').text
		if args.annotation_name == labelName:
			xmlEdited = True
			print(' - Removing object {}'.format(labelName))
			root.remove(obj)
	
	if xmlEdited:
		with open(file, 'w') as file:
			file.write(ET.tostring(root, encoding='unicode'))
	