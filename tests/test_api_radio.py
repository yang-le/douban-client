# -*- coding: utf-8 -*-

import os
import sys

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)


from douban_client import DoubanClient

client = DoubanClient(None, None)

print client.radio.channels()
