import boto3
import datetime
import time

def generate_s3_dir_path():
    """Generate timestamped path for s3 bucket"""
    base_dir = 'test_images/'
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    s3_path = base_dir+st+'/'
    return s3_path

def test_image(local_path,s3_path):
    """Uploads image to S3, informs webapp of s3 path, downloads tested image from s3
    Params:
        local_path
        s3_path
    Returns: 
        s3_path
    """
    #s3 creds YOU NEED AWS creds set up on device
    BUCKET_NAME = 'trialbucketportaltech' # replace with your bucket name
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    # upload jpg to s3 -- numpy array may be faster in the future
    s3.meta.client.upload_file(local_path, BUCKET_NAME,s3_path)
