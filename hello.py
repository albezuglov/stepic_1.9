#!/usr/bin/python
import os
import logging
#from urlparse import parse_qs

logging.basicConfig(filename='hello.log',level=logging.DEBUG)
#logging.warning('Watch out!') # will print a message to the console
#logging.info('I told you so') # will not print anything
WORK_DIR = os.path.dirname(os.path.realpath(__file__))
logging.info ( WORK_DIR)


def application(env, start_response):
    logging.info ( 'BLA BLA')
    for k, v in env.items():
        logging.info('%s: %s' % (k,v))
    logging.info ( 'BLA1 BLA1')
    #query = '\n'.join(env['QUERY_STRING'].split('&')) + '\n\n\n'
    query = env['QUERY_STRING'].split('&')
    logging.info('%s' % query)
    start_response('200 OK', [('Content-Type', 'text/plain'), ('Content-Length', len(query))])
    return query
