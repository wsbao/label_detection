"""
This script uses the Vision API's label detection capabilities to find a label
based on an image's content.
Replace "# YOUR API KEY #" with your own Google API key.
Run the script on an image to get a label, e.g.:
    ./label.py <path-to-image>
"""

import argparse
import base64
import requests
import json

def main(photo_file):

	API_KEY = # YOUR API KEY #
	
	with open(photo_file, 'rb') as image:
		image_content = base64.b64encode(image.read())
		req_data = json.dumps({
			"requests": [{
				"features": [{
					"type": "LABEL_DETECTION",
					"maxResults": 20
				}], 
				"image": {
					"content": image_content.decode('UTF-8')
				}
			}]
		})

		resp_data = requests.post("https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY, data=req_data)

		print(resp_data.text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)
