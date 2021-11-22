# -*- coding: utf-8 -*-

import json
import logging
import random
import time

HELLO_WORLD = b'Hello world!\n'

# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
# def initializer(context):
#    logger = logging.getLogger()
#    logger.info('initializing')


def handler(environ, start_response):
    context = environ['fc.context']
    request_uri = environ['fc.request_uri']
    for k, v in environ.items():
        if k.startswith('HTTP_'):
            # process custom request headers
            pass

    options = {
        '汉堡王': 1,
        '金拱门': 1,
        '杨国福': 1,
        '包子铺': 1,
        '永和': 1,
        '试试新的': 0.5,
        '点外卖': 0.5,
    }

    random.seed(time.time())
    res = random.choices(population=list(options.keys()), weights=list(options.values()), k=1)
    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    start_response(status, response_headers)

    return [res[0].encode('utf-8')]
