#!/usr/bin/env python

import requests
import re

username = 'nastas0'
password = username

url = url = 'http://{}.natas.labs.overthewire.org/'.format(username)

response = requests.get(url, auth = (username, password))
content = response.text
print(re.findall('The password for natas.* is (.*) -->',content)[0])