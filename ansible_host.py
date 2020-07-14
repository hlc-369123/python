#!/usr/bin/env python
#coding:utf8
import json
import sys
import argparse
import subprocess
import time
import threading
h = []
def ping(host):
    result = subprocess.call(
        'ping -f -c2 %s &> /dev/null' % host, shell=True
    )
    if result == 0:
       h.append(host)
def lists():
    region = {}
    region['hosts'] = dict
    return json.dumps(region, indent=4)
def hosts(name):
    region = {'ansible_ssh_user':'root', 'ansible_ssh_pass':'vagrant', 'ansible_ssh_port': 22,}
    return json.dumps(region)

if __name__ == "__main__":
    ips = ['10.255.20.%s' % i for i in range(121,124)]
    for ip in ips:
        t = threading.Thread(target=ping, args=[ip])
        t.start()
        time.sleep(0.01)
    dict={}
    for num,item in enumerate(h,start=1):
        dict["node" + str(num)] = [item]
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='hosts list', action='store_true')
    parser.add_argument('-H', '--host', help='hosts vars')
    args = vars(parser.parse_args())

    if args['list']:
        print(lists())
    elif args['host']:
        print(hosts(args['host']))
    else:
        parser.print_help()
