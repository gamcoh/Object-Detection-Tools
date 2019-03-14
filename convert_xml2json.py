
from lxml import etree
from glob import iglob
import os
import json

XMLS_DIR = 'annotations/xmls'
XMLS_DIR_PATTERN = os.path.join(
	os.path.dirname(__file__),
	'{}/*.xml'.format(XMLS_DIR)
)
JSON_FILE = 'annotations/annotations.json'

def main():
	with open(JSON_FILE) as file:
		json_content = json.load(file)

	labels_names = []
	
	for xml_file in iglob(XMLS_DIR_PATTERN):
		with open(xml_file) as file:
			print(xml_file)

			annotations = etree.fromstring(file.read())
			image_filename = annotations.find('filename').text
			boxes = annotations.iterfind('object')

			labels = []

			for box in boxes:
				label_name = box.find('name').text
				bndbox = box.find('bndbox')
				xmin = bndbox.find('xmin').text
				ymin = bndbox.find('ymin').text
				xmax = bndbox.find('xmax').text
				ymax = bndbox.find('ymax').text

				if label_name not in labels_names:
					labels_names.append(label_name)

				labels.append({
					'x': xmin,
					'x2': xmax,
					'y': ymin,
					'y2': ymax,
					'label': label_name
				})
			
			json_content['annotations'][image_filename] = labels
	
	json_content['labels'] = labels_names

	with open(JSON_FILE, 'w') as file:
		json.dump(json_content, file, indent=2)

if __name__ == "__main__":
	main()
