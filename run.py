import requests
import sys
import time

urls = ['https://ninym.top']

for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print(f'No.{i} Wakeup Status: {urls[i]} ', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
