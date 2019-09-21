#!/usr/bin/env python
#coding:utf-8


DOCUMENTATION='''
---
module: floating
short_description: This module pull floating ipaddress from openstack
description:
  - This modules pull floating ipaddress from openstack
version_added: "1.1"
options:
  username:
    description:
      - openstack auth username
    required: true
    default: admin
  password:
    description:
      - openstack tenant information
    required: true
    default: admin
  authurl:
    description:
      - openstack authurl
  required: true
  default: http://10.8.6.2:35357/v2.0/
author: Can Shen
requirements: [ "python-novaclient >= 2.20.0" ]
'''

EXAMPLES = '''
- name: pull floating ip address
  local_action: floating
                username={{ login_username }} password={{ login_password }}
                tenant={{ login_tenant_name }} authurl={{ auth_url }}
  register: floating_ip
'''


import sys
import json
import os, commands
from ansible.module_untils.basic import *
from novaclient.v1_1 import client


def main():
    module = AnsibleModule(
        argument_spec = dict(
                username = dict(default='admin', type='str'),
                password = dict(default='password', type='str'),
                tenant = dict(default='admin', type='str'),
                authurl = dict(default="http://10.8.6.2:35357/v2.0/", type="str")
         
        ),
        supports_check_mode=True
    )
    
    USER, PASS, TENANT, AUTH_URL = (
                                        module.params['username'],
                                        module.params['password'],
                                        module.params['tenant'],
                                        module.params['authurl']
    )
    
    openstack = client.Client(USER, PASS, TENANT, AUTH_URL, service_type="compute")
    
    ips = []
    for i in openstack.floating_ips.list():
        if i.fixed_ip is None:
            ips.append(i.ip)
            
    floating_ip=str(ips[0])
    
    if not floating_ip:
        print json.dumps(
            {
                "failed": True,
                "msg": "not have floating_ip"
            }
            
        )
        sys.exit(1)
    
    print json.dumps(
        {
            "res": floating_ip,
            "changed": True
        }
    )
    
    
    sys.exit(0)
    
main()
        
                                    
