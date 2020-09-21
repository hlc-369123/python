#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/22
# 删除指定对象

import boto3,json
import logging
from botocore.exceptions import ClientError

class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def delete_object(self, bucket_name, key_name):
        try:
            response = self.client.delete_object(
                Bucket=bucket_name,
                Key=key_name
            )
            print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ':')))
        except ClientError as e:
            logging.error(e)
            return False
        return response

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    conn.delete_object("bucket-1","/Users/hanlichao/Downloads/sds4.2-csi2.3.1-k8s1.17.mp4")