#! /usr/bin/env python2
# -*- coding:utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/4/26

import os,sys,json
os.system("ceph osd pool ls")
pool_name = raw_input('pool_name>>>: ').strip()
if_pool = os.popen("ceph osd pool ls|grep %s" % pool_name).read().strip()
if pool_name != if_pool:
    print "cat't find %s pool" % pool_name
    sys.exit(0)

volume_list = os.popen("rbd ls %s" % pool_name).read().strip()
volume_file = open("/tmp/volume_list","w")
volume_file.write(volume_list)
volume_file.close()

volume_file = open("/tmp/volume_list","r")
volume_size_to = 0
for volume in volume_file.readlines() :
    volume_info = json.loads(os.popen("rbd info %s/%s --format json" %(pool_name,volume.strip())).read())
    volume_size = volume_info["size"]
    volume_size_to += volume_size
volume_size_to = volume_size_to/1024/1024/1024
print "pool_name: %s,volume_size: %s GB" % (pool_name,volume_size_to)
