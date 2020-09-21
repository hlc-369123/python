#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/21
# 必须以二进制模式打开文件，和upload_file功能一致；

import boto3
import logging
from botocore.exceptions import ClientError


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def upload_fileobj(self, file_name, bucket):
        with open(file_name, "rb") as f:
            try:
                self.client.upload_fileobj(f, bucket, file_name)
            except ClientError as e:
                logging.error(e)
                return False
            return True

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    response = conn.upload_fileobj('filetest10M', 'bucket-xxx2')
    print(response)