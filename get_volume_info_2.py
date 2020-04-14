#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import os,sys,json
username = raw_input('ui_username>>>: ').strip()
password = raw_input('ui_password>>>: ').strip()
if len(username)!=0 and len(password)!=0 :
    flag = os.popen("if ! xms-cli --user %s --password %s host list &>/dev/null;then echo 'false';fi" %(username,password)).read().strip()
    if flag == 'false' :
        print "Wrong information..."
        sys.exit(0)
else :
    print "Value is empty...!"
    sys.exit(0)
volume_id = os.popen("xms-cli --user %s --password %s block-volume list|awk '{if($2  ~ /^[0-9]/) printf $2" "}'" %(username,password)).read()
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
