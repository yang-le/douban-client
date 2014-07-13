# -*- coding: utf-8 -*-

from .base import DoubanAPIBase, DEFAULT_START, DEFAULT_COUNT


class Radio(DoubanAPIBase):

    def __init__(self, access_token):
        self.access_token = access_token
        self.access_token.client.site = 'http://www.douban.com/j/app/radio'
        
    def __repr__(self):
        return '<DoubanAPI Radio>'
    
    def channels(self):
        return self._get('/channels')


    