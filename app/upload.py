import boto3
import os
from os import path

EVENT_BUCKET = os.environ["EVENT_BUCKET"]
EVENT_OBJECKT_KEY = os.environ["EVENT_OBJECKT_KEY"]

DESTINATION_BUCKET = os.environ["DESTINATION_BUCKET"]
DESTINATION_OBJECKT_DIR = os.environ["DESTINATION_OBJECKT_DIR"]

s3 = boto3.resource("s3")

destination_object_key = path.join(
    DESTINATION_OBJECKT_DIR, path.basename(EVENT_OBJECKT_KEY)
)
event_object = s3.Object(DESTINATION_BUCKET, destination_object_key)
event_object.copy({"Bucket": EVENT_BUCKET, "Key": EVENT_OBJECKT_KEY})