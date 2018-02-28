#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'cyrus'

# 查询港澳通行证申请状态

import requests
import commands

class GZTXZ(object):
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'User-Agent' : 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            }
        url = 'http://www.gdcrj.com/gdwssq/ajax?method=init'
        data = {'ywlx':22}
        r = self.session.post(url,headers=self.headers,data=data)

    def get_status(self,sfz):
        url='http://www.gdcrj.com/gdwssq/ajax?method=progressCxPrint'
        data = {
            'slbh':sfz,
            'ywlx':'22',
            }
        r = self.session.post(url,headers=self.headers,data=data)
        return r.text.encode('utf-8')[15:-2]



if __name__ == '__main__':
    sfz = '120101200001014937'
    txz = GZTXZ()
    print txz.get_status(sfz)