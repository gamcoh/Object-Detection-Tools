# xml → json
Converts PASCAL VOC annotations to the \_annotations.json format supported by the Cloud Annotations tool.

## Instructions
Install the Cloud Object Storage SDK:
```
pip install botocore==1.12.26 ibm-cos-sdk==2.3.2 ibm-cos-sdk-core==2.3.2 ibm-cos-sdk-s3transfer==2.3.2
```

Convert xml annotations to json:
```
python convert_xml2json.py
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

Upload images and annotations to Cloud Object Storage Bucket:
```
python upload2bucket.py
```
