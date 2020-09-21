#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/22
# 指定个数列出对象

import boto3,logging
from botocore.exceptions import ClientError

class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def list_object(self,bucket_name, maxkeys):
        try:
            response = self.client.list_objects_v2(
                Bucket=bucket_name,
                MaxKeys=maxkeys
            )
            print(response)
        except ClientError as e:
            logging.error(e)
            return False
        return response

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    conn.list_object("bucket-1",2)