#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<i@binux.me>
#         http://binux.me
# Created on 2014-02-15 22:10:35

import time
import unittest


from fetcher.tornado_fetcher import Fetcher
class TestTaskDB(unittest.TestCase):
    sample_task_http = {
            'taskid': 'taskid',
            'project': 'project',
            'url': 'http://my.zzti.edu.cn/loginPortalUrl.portal',
            'fetch': {
                'method': 'POST',
                'headers': {
                    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
                                               'Accept-Encoding':'gzip, deflate','Origin':'http://my.zzti.edu.cn',
                                               'Content-Type':'application/x-www-form-urlencoded'
                    },
                'data':"userName=201100834224&password=280036",
                'timeout': 60,
                #'allow_redirects':False
                },
            'process': {
                'callback': 'callback',
                'save': [1, 2, 3],
                },
            }
    def test_http_get(self):
        fetcher = Fetcher(None, None, proxy={'http':'127.0.0.1:8080'},async=False)
        def callback(type, task, result):
            print result
            print result['content']
            #self.assertEqual(task, self.sample_task_http)
            #self.assertEqual(result['status_code'], 200)
            #self.assertEqual(result['orig_url'], self.sample_task_http["url"])
            #self.assertIn("a=b", result['content'])
        fetcher.fetch(self.sample_task_http, callback=callback)
