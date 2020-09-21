#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/22
# 分段上传

import boto3,logging
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def upload_file_mult(self, file_name, bucket, object_name=None):
        MB = 1024 ** 2
        config = TransferConfig(multipart_threshold=8 * MB)
        if object_name is None:
            object_name = file_name
        try:
            self.client.upload_file(file_name, bucket, object_name, Config=config)
        except ClientError as e:
            logging.error(e)
            return False
        return True

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    response = conn.upload_file_mult("/Users/hanlichao/Downloads/sds4.2-csi2.3.1-k8s1.17.mp4","bucket-1")
    print(response)