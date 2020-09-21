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

    def download_file(self, bucket, object_name, file_name=None):
        if file_name is None:
            file_name = object_name
        try:
            self.client.download_file(bucket, object_name, file_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    response = conn.download_file('bucket-xxx2', 'filetest10M', 'filetest10M2')
    print(response)