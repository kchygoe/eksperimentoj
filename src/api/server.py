#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright(c) 2015 Koichi Yoshigoe <yoshigoe@d-red.jp>
#
__author__ = "Koichi Yoshigoe"
__copyright__ = "Copyright(c) 2015 Koichi Yoshigoe <yoshigoe@d-red.jp>"

from tornado.options import define, options
import tornado.options
import tornado.ioloop
import tornado.web
import os.path
import sys
import logging
import json
from redis import Redis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

define(
    'port',
    default=8888,
    metavar='true|false',
    help='http port')

class Error(Exception):
  """General Error for this package."""
  pass


class IllegalArgumentError(Error):
  """Thrown when an illegal argument is specified."""
  pass


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        logger.info(self, "HelloHandler")

class IndexHandler(tornado.web.RequestHandler):
  def get(self):
    self.render('index.html')

def ServerLoop(port, handlers):
  app = tornado.web.Application(handlers)
  logging.info('Listening %d', port)
  app.listen(port)

  tornado.ioloop.IOLoop.instance().start()

_parsed_args = None

def ParseOptions():
  """Parses command line options."""
  global _parsed_args
  if _parsed_args is None:
    _parsed_args = tornado.options.parse_command_line()
    logging.info('Starting %s', sys.argv[0])
  return _parsed_args

#redisconnect = redis.Redis(host='localhost', socket_timeout=5)
app = tornado.web.Application([
  (r"/vm/(.*)", InfoVmHandler),
  (r"/vms", InfoVmsHandler),
  (r"/", IndexHandler),
  (r"/info_vm/(.*)", AllInfoHandler)
  ],
  template_path=os.path.join(os.path.dirname(__file__),"../html")
)

if __name__ == "__main__":
  app.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
