#!/usr/bin/python3
import os
import logging

logging.basicConfig(filename='hello.log',level=logging.DEBUG)
logging.warning('Watch out!') # will print a message to the console
logging.info('I told you so') # will not print anything
WORK_DIR = os.path.dirname(os.path.realpath(__file__))
logging.info ( WORK_DIR)


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello!"]
