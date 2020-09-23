#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2020/9/23 14:36
@Auth ： 
"""
#分段上传，MD5效验；

import boto3, hashlib, base64,logging,json
from botocore.exceptions import ClientError

#计算分段MD5函数
def content_encoding(str):
    content_md5 = hashlib.md5()
    content_md5.update(str)
    content_base64 = base64.b64encode(content_md5.digest())
    return content_base64.decode("utf-8")


class CONNECTION(object):
    def __init__(self, url=None):
        self.client = boto3.client('s3', endpoint_url=url)

    def create_mulitipart_upload(self, bucket_name=None, file_path=None, file_name=None, key=None):
        try:
            upload_id = self.client.create_multipart_upload(Bucket=bucket_name, Key=key)["UploadId"]

            MB = 1024 ** 2
            # upload_part接口限制，除最后一个分片之外，其他的分片要大于等于5MB；
            slice_size = 8 * MB

            with open(file_path + file_name, 'rb') as data:
                #Part numbers的范围为1~10,000；
                index = 0
                while True:
                    index += 1
                    part = data.read(slice_size)
                    if not part:
                        break
                    else:
                        #计算每个分段的MD5值；
                        file_MD5 = content_encoding(part)
                        print(index, file_MD5)
                    #上传分片
                    self.client.upload_part(Bucket=bucket_name
                                            , Key=key
                                            , PartNumber=index
                                            , UploadId=upload_id
                                            , ContentMD5=file_MD5
                                            , Body=part)
            #获取UploadId对应的分片；
            Parts = self.client.list_parts(Bucket=bucket_name, Key=key, UploadId=upload_id)["Parts"]

            #生成分片列表
            partETags = []
            for k in Parts:
                partETags.append({"PartNumber": k.get("PartNumber"), "ETag": k.get("ETag")})
            # MultipartUpload必须字典；
            part_info = {}
            part_info["Parts"] = partETags
            response = self.client.complete_multipart_upload(Bucket=bucket_name
                                                        , Key=key
                                                        , UploadId=upload_id
                                                        , MultipartUpload=part_info)
            print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ':')))
        except ClientError as e:
            logging.error(e)
            return False
        return response

if __name__ == '__main__':
    # url = "http://172.16.68.100:7480"
    url = "http://10.255.20.121:7480"
    conn = CONNECTION(url)
    conn.create_mulitipart_upload("bucket-1","./","file16M","file16M")
