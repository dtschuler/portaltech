import boto3
import datetime
import time
import os
import urllib.request
import json

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

def test_image_demo(local_dir_path):
    """Uploads both images to S3, informs webapp of s3 path, downloads tested image from s3
    Params:
        local_path
    Returns: 
        local_tested_image
    """
    s3_dir_path = generate_s3_dir_path()
    image_state_list = ['open','close']
    base_file = os.path.basename(local_dir_path)
    BUCKET_NAME = 'trialbucketportaltech' # replace with your bucket name
    #s3 creds YOU NEED AWS creds set up on device
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    for state in image_state_list:
        local_path = local_dir_path+state+'.jpg'
        s3_path = s3_dir_path+state+'.jpg'
        # upload jpg to s3 -- numpy array may be faster in the future
        s3.meta.client.upload_file(local_path, BUCKET_NAME, s3_path)
    #send path to webapp and get s3 locations of tested image
    inference_return_json = send_path_to_demo_objdet(s3_dir_path).decode("utf-8") 
    print(inference_return_json)
    inference_return_dict = json.loads(inference_return_json)
    #download tested image
    for state in image_state_list:
        local_tested_image_path = '/tmp/tested'+state+'.jpg'
        dict_image_string = state+'_tested_path'
        tested_image_s3_path = inference_return_dict[dict_image_string]
        s3.meta.client.download_file(BUCKET_NAME, tested_image_s3_path, local_tested_image_path)

    
