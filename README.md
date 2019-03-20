# 🔧 Object-Detection-Tools
Tools for object detection annotations in machine learning:
- Converts PASCAL VOC annotations to the \_annotations.json format supported by the Cloud Annotations tool.
- Upload images and annotations to Cloud Object Storage Bucket.
- Converts PASCAL VOC annotations to the COCO json annotation format.

## Instructions
### Remove some annotation
This script removes an annotation from all of your xml files.
If you want to remove all xml objects from your annotations files that have the label 'car':
```
python remove_annotation.py --name car
```

### xml → json (Cloud Annotations Tool)
Convert xml annotations to json:
```
python convert_xml2json.py
```

### xml → json (COCO json annotation format)
Convert xml annotations to coco json annotation format
```
python pascal_voc_xml2coco_json.py
```

### Upload images and annotations to Cloud Object Storage Bucket
Install the Cloud Object Storage SDK:
```
pip install botocore==1.12.26 ibm-cos-sdk==2.3.2 ibm-cos-sdk-core==2.3.2 ibm-cos-sdk-s3transfer==2.3.2
```

Add your `credentials` to `upload2bucket.py`:
```python
credentials = {
  'bucket': 'YOUR_BUCKET_NAME',
  'iam_url': 'https://iam.ng.bluemix.net/oidc/token',
  'resource_instance_id': 'YOUR_INSTANCE_ID',
  'url': 'YOUR_REGION_ENDPOINT',
  'api_key': 'YOUR_API_KEY'
}
```

Upload the images and the annotations:
```
python upload2bucket.py
```

## Acknowledgments
- Thanks to [@bourdakos1](https://github.com/bourdakos1) for the great help
- Thanks to [@CivilNet](https://github.com/CivilNet) for the xml to coco script
