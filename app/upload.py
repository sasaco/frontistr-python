import boto3
import os
from os import path
import glob

print('解析結果ファイルのアップロードを開始します!!')

# 出力フォルダS3を取得
DESTINATION_BUCKET = os.environ["DESTINATION_BUCKET"]
s3 = boto3.resource("s3")
bucket = s3.Bucket(DESTINATION_BUCKET)

# 出力データを収集する
files = glob.glob("/tmp/*")

# 解析結果ファイルを出力フォルダS3にコピー
for path in files:
    filename = os.path.basename(path)

    # 解析結果に関係ないファイルは除外する
    if filename == 'run.sh' or filename == 'download.py' or filename == 'upload.py':
        continue

    bucket.upload_file(path, filename)

print('解析結果ファイルのアップロードに成功しました!!')