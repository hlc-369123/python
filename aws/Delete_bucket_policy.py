#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/20
# 删除策略

import logging
import boto3,json
from botocore.exceptions import ClientError


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def delete_bucket_policy(self, bucket_name=None):
        try:
            response = self.client.delete_bucket_policy(Bucket=bucket_name)
            print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ':')))
        except ClientError as e:
            logging.error(e)
            return False
        return response

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    conn.delete_bucket_policy("bucket01")