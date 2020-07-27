import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = ['https://bili33.top']
for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print(f'No.{i} Wakeup Status: ', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
