import time

import redis
from flask import Flask

import os

# Set environment variables
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

app = Flask(__name__)


cache = redis.Redis(host=REDIS_HOST, port=6379, password=REDIS_PASSWORD)

#Removing literal setting and change to env values
#cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
