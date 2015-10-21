#!/usr/bin/python
# coding:utf-8
#author:sunrain
#       tdifg.com
#Create on 15/10/20

from tornado.httpclient import HTTPClient,AsyncHTTPClient,HTTPRequest
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop

def synchronous_fetch(url):
    http_client = HTTPClient()

    response = http_client.fetch(url)
    return response

#print synchronous_fetch("http://www.baidu.com")

def printbody(body):
    print body.body

def async_fetch(url):
    http_client = AsyncHTTPClient()
    if not isinstance(url,list):
        url = [url]
    for u in url:
        http_client.fetch(u,printbody)
    #IOLoop.instance().start()

#async_fetch('http://www.baidu.com')

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