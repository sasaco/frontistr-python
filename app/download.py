import boto3
import os
import shutil

# 入力データ(zipファイル)の保存場所S3を取得
EVENT_BUCKET = os.environ["EVENT_BUCKET"]
EVENT_OBJECKT_KEY = os.environ["EVENT_OBJECKT_KEY"]
s3 = boto3.resource("s3")
bucket = s3.Bucket(EVENT_BUCKET)

# zipファイルの保存場所を決める
zip_filepath = '/tmp/' + EVENT_OBJECKT_KEY.split('/')[-1]

# zipファイルを取得する
s3.download_file(bucket, EVENT_OBJECKT_KEY, zip_filepath)

# zipファイルを解凍する
shutil.unpack_archive(zip_filepath, '/tmp/')

