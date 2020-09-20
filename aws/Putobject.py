#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/15 18:46
@Auth ：
"""
# 上传对象

from boto3.session import Session
from datetime import datetime
import warnings,json,hashlib,base64
warnings.filterwarnings("ignore", category=UnicodeWarning)


class CONNECTION(object):
    def __init__(self, access_key=None, secret_key=None, url=None):
        self._access_key = access_key
        self._secret_key = secret_key
        self._url = url
        self._session = Session(self._access_key, self._secret_key)
        self.client = self._session.client('s3', endpoint_url=self._url)

    def put_object(self, bucket_name=None, file_name=None):
        file_handle = open(file_name, 'rb')
        content_md5 = hashlib.md5()
        content_md5.update(file_handle.read())
        content_base64 = base64.b64encode(content_md5.digest())
        file64_md5 = content_base64.decode("utf-8")
        print(file64_md5)

        response = self.client.put_object(
            ACL="private",   # 'private' | 'public-read' | 'public-read-write' | 'authenticated-read' | 'aws-exec-read' | 'bucket-owner-read' | 'bucket-owner-full-control',
            Body=file_handle, # b'bytes' | file,
            Bucket=bucket_name, #'string',
            ContentMD5=file64_md5, #'string', base64
            Expires=datetime(2022, 1, 1),
            Key="file_name", #"'string',
            Metadata={
                'string': 'string1'
            },
            ServerSideEncryption='AES256',# | 'aws:kms',
            StorageClass='STANDARD'#'STANDARD' | 'REDUCED_REDUNDANCY' | 'STANDARD_IA' | 'ONEZONE_IA' | 'INTELLIGENT_TIERING' | 'GLACIER' | 'DEEP_ARCHIVE',
        )
        file_handle.close()
        print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ':')))
        return response
if __name__ == '__main__':
    access_key = "12345678901234567890"
    secret_key = "1234567890123456789012345678901234567890"
    url = "http://172.16.68.100:7480"
    conn = CONNECTION(access_key, secret_key, url)
    conn.put_object('bucket-1','../S3demon/filetest10M')