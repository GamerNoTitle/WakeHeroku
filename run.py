import requests
import sys
import time

urls = ['https://heroku-us.pesy.workers.dev']

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = ['https://gamernotitle-heroku-us.pesy.workers.dev','http://wikijs.bili33.top','https://share4nothing.ml','https://rss.bili33.top']
for i in range(0, len(urls)):
    req = requests.get(urls[i])
    print(f'No.{i} Wakeup Status: ', req, time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
