#!/usr/bin/env python
#coding:utf8

from jinjia2.filter import environmentfilter
from ansible import errors
import time


def string(str, seperator=' '):
    return str.split(seperator)
    
    
def _time(times):
    return time.mktime(time.strptime(times, "%Y-%m-%d %H:%M:%S"))
    

class FilterModule(object):
    ''' Ansible custom filter '''
    
    
    def  filters(self):
        return {
            'myfilter1': string,
            'myfilter2': _time
        }
        
        
