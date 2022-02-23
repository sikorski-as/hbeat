from time import sleep
from os import environ

import requests

HBEAT_URL = environ.get("HBEAT_URL")
HBEAT_TOKEN = environ.get("HBEAT_TOKEN")

while True:
    requests.post(f'{HBEAT_URL}?token={HBEAT_TOKEN}')
    sleep(5)
