import json
import glob
import subprocess
import os
import time

def handler(event, context):

    cnt_path = '/function/tmp/hinge.cnt'
    mesh_path = '/function/tmp/hinge.mesh'
    res_path = '/function/tmp/hinge.res.*'
    vis_path = '/function/tmp/hinge_vis_*'

    """
    # 引数
    if "body" in event:
        js = json.loads(event["body"])
    else:
        js = event
    cnt = js['cnt']
    mesh = js['mesh']

    # .cnt ファイルを 書き込む
    fout=open(cnt_path, 'w')
    print(cnt, file=fout)
    fout.close()

    # .mesh ファイルを 書き込む
    fout=open(mesh_path, 'w')
    print(mesh, file=fout)
    fout.close()
    """

    # FrontISTR で 計算する
    os.chdir('/function/tmp')
    proc = subprocess.call('fistr1', shell=True)

    # 書き込んだ .res ファイルを 読み込む
    res = []
    for r in glob.glob(res_path):
        f = open(r)
        res.append(f.read())  # ファイル終端まで全て読んだデータを返す
        f.close()

    # 返す
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin":"*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "res": res,
        }),
    }