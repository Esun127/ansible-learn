#!/usr/bin/env python
#coding:utf8


"""
Description: This lookup query value from mysql
Example Usage:
{{ lookup('mysql',('192.168.1.117', 'Ansible', 'lookup', 'ansible')) }}
"""

from ansible import utils, errors

HAVE_MYSQL = False
try:
    import MySQLdb
    HAVE_REDIS = True
except ImportError:
    pass
    
    
    
class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir
        
        if HAVE_REDIS == False:
            raise errors.AnsibleError("Can't LOOKUP(mysql): module MySQLdb is not installed")
            
    
    def run(self, terms, inject=None, **kwargs):
        terms = utils.listfy_lookup_plugin_terms(terms, self.basedir, inject)
        ret = []
        host, db, table, key=(terms[0], terms[1], terms[2], terms[3])
        conn = MySQLdb.connect(host=host, user='root', passwd='123456', db=db, port=3306)
        cur = conn.cursor()
        sql = 'select value from %s where keyname = "%s"' %(table, key)
        cur.execute(sql)
        result = cur.fetchone()
        if result[0]:
            ret.append(result[0])
            return ret
        else:
            return None
