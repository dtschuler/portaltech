import boto3
import datetime
import time
import os
import urllib.request

def generate_s3_dir_path():
    """Generate timestamped path for s3 bucket"""
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    s3_path = 'images/'+st+'/'+'test_images/'
    return s3_path

def send_path_to_demo_objdet(s3_path):
    url_str = 'http://portalobjectdetection.us-east-1.elasticbeanstalk.com/'+'detection/'+s3_path
    tested_image_path = urllib.request.urlopen(url_str).read()
    return tested_image_path

def test_image_demo(local_path):
    """Uploads image to S3, informs webapp of s3 path, downloads tested image from s3
    Params:
        local_path
    Returns: 
        local_tested_image
    """
    s3_dir_path = generate_s3_dir_path()
    base_file = os.path.basename(local_path)
    s3_path = s3_dir_path+base_file
    #s3 creds YOU NEED AWS creds set up on device
    BUCKET_NAME = 'trialbucketportaltech' # replace with your bucket name
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    # upload jpg to s3 -- numpy array may be faster in the future
    s3.meta.client.upload_file(local_path, BUCKET_NAME, s3_path)
    #send path to webapp and get s3 locations of tested image
    tested_image_path = send_path_to_demo_objdet(s3_path).decode("utf-8") 
    #download tested image
    local_tested_image_path = 'test-images/tested_image'
    s3.meta.client.download_file(BUCKET_NAME, tested_image_path, local_tested_image_path)

    
