# -*- coding: utf-8 -*-

from .base import DoubanAPIBase, DEFAULT_START, DEFAULT_COUNT


class Radio(DoubanAPIBase):

    def __init__(self, access_token):
        self.access_token = access_token
        self.access_token.client.site = 'http://www.douban.com/j/app/radio'
        self.user_id = ''
        self.expire = ''
        self.token = ''
        
    def __repr__(self):
        return '<DoubanAPI Radio>'
    
    def channels(self):
        return self._get('/channels')

    def people(self, type, channel_id, song_id, history):
        return self._get('/people',
                         app_name = 'radio_desktop_win',
                         version = 100,
                         user_id = self.user_id,
                         expire = self.expire,
                         token = self.token,
                         sid = song_id,
                         h = history,
                         channel = channel_id,
                         type = type)

    # 不再播放
    def bye(self, channel_id, song_id, h = ''):
        return self.people('b', channel_id, song_id, h)
    
    # 停止播放
    def end(self, channel_id, song_id, h = ''):
        return self.people('e', channel_id, song_id, h)
    
    # 取得播放列表
    def new(self, channel_id, song_id = '', h = ''):
        return self.people('n', channel_id, song_id, h)

    # 返回播放列表？
    def playing(self, channel_id, song_id, h = ''):
        return self.people('p', channel_id, song_id, h)
    
    # 跳过
    def skip(self, channel_id, song_id, h = ''):
        return self.people('s', channel_id, song_id, h)
    
    # 喜欢
    def rate(self, channel_id, song_id, h = ''):
        return self.people('r', channel_id, song_id, h)
    
    # 取消喜欢
    def unrate(self, channel_id, song_id, h = ''):
        return self.people('u', channel_id, song_id, h)
    
