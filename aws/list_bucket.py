#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/20
# 列出存储桶的名称

import boto3


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.resource('s3', endpoint_url=url)

    def list_bucket(self):
        # print(self.client.buckets.all())
        for bucket in self.client.buckets.all():
            print(bucket.name)


if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    conn.list_bucket()