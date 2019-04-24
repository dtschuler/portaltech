import sys

sys.path.append('object_detectionAPI')
from objdetect_utils import test_image_demo

images_dir = 'object_detectionAPI/test-images/tmp/'
test_image_demo(images_dir)