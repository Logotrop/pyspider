#!/usr/bin/python
# coding:utf-8
#author:sunrain
#       tdifg.com
#Create on 15/10/20

from tornado.httpclient import HTTPRequest
from tornado.curl_httpclient import CurlAsyncHTTPClient
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop


#print synchronous_fetch("http://www.baidu.com")

def printbody(rp):
    print rp.headers
    print rp.body
    print rp.code
    print rp.error
    print rp.time_info


def async_fetch(url):
    http_client = CurlAsyncHTTPClient()
    rq = HTTPRequest(url,method='POST',headers={"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
                                               'Accept-Encoding':'gzip, deflate','Origin':'http://www.douban.com',
                                               'Content-Type':'application/x-www-form-urlencoded'},body="source=index_nav&form_email=ymmxza%40gmail.com&form_password=3jpnd%2442")
    http_client.fetch(rq,callback=printbody)
    IOLoop.instance().start()
    http_client.close()


async_fetch('https://www.douban.com/accounts/login')

'''
headers= {
    'url':'http://www.baidu.com',
                'method': 'GET',
                'headers': {
                    'Cookie': 'a=b',
                    'a': 'b'
                    },
                #'data': '',
                'connect_timeout': 60,
                }

realheader = HTTPHeaders()

def handleheader(line):
    line = line.strip()
    if line:
        if line.startswith("HTTP/"):
            return
        #print line

        realheader.parse_line(line)

rq = HTTPRequest(header_callback=handleheader,**headers)

async_fetch(rq)


print 'asdf'

asdf = 'asdfasdf'
'''

'''
from UserDict import DictMixin

class Test(DictMixin):

    __slot__ = ['name','age','gender']
    __getitem__ = lambda *x:getattr(*x)
    __setitem__ = lambda *x:setattr(*x)

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


t = Test('a',23,True)

print t.name

t.name = 'asdfasdf'

print t.name
'''