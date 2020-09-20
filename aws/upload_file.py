#! /usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ : Hlc
#__date__   : 2020/9/20
# 下载一个文件，并显示下载进度

import sys,os,threading,boto3
from s3transfer import S3Transfer

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    transfer = S3Transfer(boto3.client('s3', endpoint_url = url))
    # Upload /tmp/myfile to s3://bucket/key and print upload progress.
    transfer.upload_file('/Users/hanlichao/Downloads/eclipse-jee-2020-06-R-macosx-cocoa-x86_64.dmg', 'bucket-xxx', 'filetest10M',
                         callback=ProgressPercentage('/Users/hanlichao/Downloads/eclipse-jee-2020-06-R-macosx-cocoa-x86_64.dmg'))

