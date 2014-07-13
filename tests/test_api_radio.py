# -*- coding: utf-8 -*-

import os
import sys

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)


from douban_client import DoubanClient

client = DoubanClient(None, None)

print client.radio.channels()
# print client.radio.new(1)
# print client.radio.playing(1, 2)
# print client.radio.end(1, 2)
# print client.radio.skip(1, 2)
# print client.radio.rate(1, 2)
# print client.radio.unrate(1, 2)
# print client.radio.bye(1, 2)
