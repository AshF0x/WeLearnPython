import requests
import argparse
import time
import os
# Downloading robots.txt every 'n'time from a webpage
# Hashing the value and comparing it
# Alarm when it changed
url = "http://www.tesla.com"
r = requests.get(url)
st_code = r.status_code

