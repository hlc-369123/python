#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : Hlc
# __date__   : 2020/9/21
# 上传文件，可以通过配置文件定义一些策略

import boto3
# from s3transfer import S3Transfer
import logging
from botocore.exceptions import ClientError


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def upload_file(self, file_name, bucket, object_name=None):
        if object_name is None:
            object_name = file_name
        try:
            self.client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    # def Upload_file(self, file_name,bucket,key):
    #     res = S3Transfer(self.client).upload_file(file_name,bucket,key)
    #     print(res)


if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    response = conn.upload_file('filetest10M', 'bucket-1', 'filetest10M2')
    print(response)
