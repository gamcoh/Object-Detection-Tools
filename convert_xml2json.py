from lxml import etree
from glob import iglob
import os
import json

XMLS_DIR = 'annotations/xmls'
XMLS_DIR_PATTERN = os.path.join(
	os.path.dirname(__file__),
	'{}/*.xml'.format(XMLS_DIR)
)
TEMPLATE = 'annotations/template.json'
OUTPUT = '_annotations.json'

def main():
	with open(TEMPLATE) as file:
		json_content = json.load(file)

	labels_names = set()
	
	for xml_file in iglob(XMLS_DIR_PATTERN):
		with open(xml_file) as file:
			print(xml_file)

			annotations = etree.fromstring(file.read())
			image_filename = annotations.find('filename').text
			boxes = annotations.iterfind('object')

			size = annotations.find('size')
			image_width = size.find('width').text
			image_height = size.find('height').text

			labels = []

			for box in boxes:
				label_name = box.find('name').text
				bndbox = box.find('bndbox')
				xmin = bndbox.find('xmin').text
				ymin = bndbox.find('ymin').text
				xmax = bndbox.find('xmax').text
				ymax = bndbox.find('ymax').text

				labels_names.add(label_name)

				labels.append({
					'x': float(xmin) / float(image_width),
					'x2': float(xmax) / float(image_width),
					'y': float(ymin) / float(image_height),
					'y2': float(ymax) / float(image_height),
					'label': label_name
				})
			
			json_content['annotations'][image_filename] = labels
	
	json_content['labels'] = list(labels_names)

	with open(OUTPUT, 'w') as file:
		json.dump(json_content, file, indent=2)

if __name__ == "__main__":
	main()
