#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : Hlc
# __date__   : 2020/9/23
# 检查并清理残留分片

import boto3, logging, json, sys
from botocore.exceptions import ClientError


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def list_multipart_uploads(self, bucket_name=None):
        try:
            #存在残留分片返回Uploads，不存在残留分片退出，并提示；
            def list_multipart_uploads(bucket_name):
                if self.client.list_multipart_uploads(Bucket=bucket_name).get("Uploads") is None:
                    print("There is no residual fragmentation！")
                    sys.exit(0)
                else:
                    return self.client.list_multipart_uploads(Bucket=bucket_name).get("Uploads")

            #若存在残留分片，则遍历并清理，以json格式返回；
            for uploads_num in range(len(list_multipart_uploads(bucket_name))):
                uploads_list = list_multipart_uploads(bucket_name)[0]
                response = self.client.abort_multipart_upload(
                    Bucket=bucket_name,
                    Key=uploads_list["Key"],
                    UploadId=uploads_list["UploadId"]
                )
                print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ':')))

        except ClientError as e:
            logging.error(e)
            return False
        return True


if __name__ == '__main__':
    url = "http://172.16.68.100:7480"
    # url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    conn.list_multipart_uploads("bucket-1")
