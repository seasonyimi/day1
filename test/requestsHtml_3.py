# 微博爬虫模拟登录
# 如何修改防止防爬
#!/bin/bash python=
# -*- coding: UTF-8 -*-
from requests_html import HTMLSession
import traceback
class GetCookies(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    # 通过fiddler抓包分析模拟登陆的form表单，获取cookies和自己账号的uid
    def get_cookies(self):
        try:
            session = HTMLSession()
            url = r'https://passport.weibo.cn/sso/login'
            post_data = {
                'username': self.username,
                'password': self.password,
                'savestate': '1',
                'r': 'https://weibo.cn/',
                'ec': '0',
                'pagerefer': 'https://weibo.cn/pub/',
                'entry': 'mweibo',
                'wentry': '',
                'loginfrom': '',
                'client_id': '',
                'code': '',
                'qq': '',
                'mainpageflag': '1',
                'hff': '',
                'hfp': ''
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
                'Host': 'passport.weibo.cn',
                'Origin': 'https://passport.weibo.cn',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Connection': 'keep-alive'
            }
            r = session.post(url=url,data=post_data,headers=headers)
            print('r=',r)
            mid = r.json()['data']['uid']
            print('mid=',mid)
            return r.cookies, mid
        except Exception as e:
            print('Error:', e)
            traceback.print_exc()

if __name__ == '__main__':
    GetCookies(1,2)