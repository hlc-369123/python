#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/4/13

import os,sys,json
volume_id = os.popen("xms-cli --user admin --password admin block-volume list|awk '{if($2  ~ /^[0-9]/) printf $2" "}'").read()
for id in volume_id :
    volume_info = os.popen( "xms-cli --user admin --password admin -f json block-volume show %s" %id).read()
    print "======================================="
    volume_info_dic = json.loads(volume_info)
    print type(volume_info_dic)
    access_path = volume_info_dic["block_volume"]["access_path"] or {}
    volume_name = volume_info_dic["block_volume"]["volume_name"]
    size = volume_info_dic["block_volume"]["size"]
    passive = volume_info_dic["block_volume"]["passive"]
    pool = volume_info_dic["block_volume"]["pool"]
    print "volume_name: %s,pool: %s,size: %s,passive: %s,access_path: %s" %(volume_name,pool["name"],size,passive,access_path.get("name"))
