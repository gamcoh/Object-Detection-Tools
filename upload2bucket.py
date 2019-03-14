import os

import ibm_boto3
from botocore.client import Config

credentials = {
  'bucket': 'YOUR_BUCKET_NAME',
  'iam_url': 'https://iam.ng.bluemix.net/oidc/token',
  'api_key': 'YOUR_API_KEY',
  'resource_instance_id': 'YOUR_INSTANCE_ID',
  'url': 'YOUR_REGION_ENDPOINT'
}

def main():
  bucket = ibm_boto3.resource('s3',
    ibm_api_key_id=credentials['api_key'],
    ibm_service_instance_id=credentials['resource_instance_id'],
    ibm_auth_endpoint=credentials['iam_url'],
    config=Config(signature_version='oauth'),
    endpoint_url=credentials['url']
  ).Bucket(credentials['bucket'])
  bucket.upload_file('_annotations.json', '_annotations.json')
  
  directory = 'images'
  for filename in os.listdir(directory):
    small = filename.lower()
    if small.endswith('.jpeg') or small.endswith('.jpg') or small.endswith('.png'):
      bucket.upload_file(os.path.join(directory, filename), filename)
      continue
    else:
      continue


if __name__ == "__main__":
  main()