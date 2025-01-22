import pymysql
import json
import boto3
from datetime import datetime

db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "wildchild94",
    "database": "webhook_db",
}

sqs = boto3.client("sqs")
QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/123456789012/YourQueueName"


def lambda_handler(event, context):
    message = json.loads(event["body"])
    msg_payload = {
        "message_id": message["id"],
        "content": message["content"],
        "user_phonenumber": message["from"],
        "created_utc": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    }

    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO messages (message_id, content, user_phonenumber, created_utc) VALUES (%s, %s, %s, %s)"
            cursor.execute(
                sql,
                (
                    msg_payload["message_id"],
                    msg_payload["content"],
                    msg_payload["user_phonenumber"],
                    msg_payload["created_utc"],
                ),
            )
        connection.commit()
    finally:
        connection.close()

    sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(msg_payload))

    return {"statusCode": 200, "body": json.dumps({"status": "Message processed"})}
