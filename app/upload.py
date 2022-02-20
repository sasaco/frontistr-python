import boto3
import os
from os import path
import glob

# 出力フォルダS3を取得
DESTINATION_BUCKET = os.environ["DESTINATION_BUCKET"]

s3 = boto3.resource("s3")
bucket = s3.Bucket(DESTINATION_BUCKET)


# 出力データを収集する
files = glob.glob("/tmp/*", recursive=True)

# 解析結果ファイルを出力フォルダS3にコピー
for filepath in files:
    filename = os.path.basename(filepath)
    path, ext = os.path.splitext(filepath)

    # 解析結果に関係ないファイルは除外する
    if ext == '.sh' or ext == '.py' or ext == '.zip':
        continue

    bucket.upload_file(filepath, filename)

