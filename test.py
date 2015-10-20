#!/usr/bin/python
# coding:utf-8
#author:sunrain
#       tdifg.com
#Create on 15/10/20

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
