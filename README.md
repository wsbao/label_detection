# label_detection
Another way to realize the label detection based on Google vision API

I followed official documentation https://cloud.google.com/vision/docs/label-tutorial to try the label detection. I downloaded the private key in JSON format, and set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of my private key. However, when I apply the “label.py” script downloaded from GitHub repository https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/api/label/label.py, it always ends up with “Timeout Error: [WinError 10060]”. So I scripted my own "getImgLabel.py" to realize label detection function.
