# -*- coding: utf-8 -*-
import pycurl
import json
from io import BytesIO
import argparse
import datetime


def post_req():
    "test post request"
    response = BytesIO()
    url = "http://192.168.128.188:8001/import"
    params = {'date': datetime.datetime.now().strftime("%Y-%m-%dS"),
              'time': datetime.datetime.now().strftime("%H:%M:%S"),
              'account': args.text}
    c = pycurl.Curl()
    c.setopt(c.CUSTOMREQUEST, "POST")
    c.setopt(c.POSTFIELDS, json.dumps(params))
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    response_code = c.getinfo(c.HTTP_CODE)
    if response_code != 200:
        pass
    else:
        message = 'Response: ' + response.getvalue()

    return message


def get_req():
    "test get req"
    response = BytesIO()
    url = "http://192.168.128.188:8001/last"
    c = pycurl.Curl()
    c.setopt(c.CUSTOMREQUEST, "GET")
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    response_code = c.getinfo(c.HTTP_CODE)
    if response_code != 200:
        pass
    else:
        message = 'Response: ' + str(json.loads(response.getvalue()))

    return message