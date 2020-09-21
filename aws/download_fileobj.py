#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/21

import boto3
import logging
from botocore.exceptions import ClientError


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def download_fileobj(self, bucket, file_name):
        with open(file_name, 'wb') as f:
            try:
                self.client.download_fileobj(bucket, file_name, f)
            except ClientError as e:
                logging.error(e)
                return False
            return True

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    response = conn.download_fileobj('bucket-xxx2', 'filetest10M')
    print(response)