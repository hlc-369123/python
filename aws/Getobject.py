#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/20
# 下载object

import boto3,json
class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def get_object(self, bucket_name=None, file_name=None):
        response = self.client.get_object(
            Bucket=bucket_name,
            Key=file_name,
            # Range='string',
            # VersionId='string',
            # RequestPayer='requester',
            # PartNumber=123
        )
        print(json.dumps(response['ResponseMetadata'], sort_keys=True, indent=4, separators=(',', ':')))
        # print(response)
        return response

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    conn.get_object("bucket01","test-key-1")