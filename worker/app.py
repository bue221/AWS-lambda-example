import pymysql
import json

db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "wildchild94",
    "database": "webhook_db",
}


def lambda_handler(event, context):
    connection = pymysql.connect(**db_config)
    try:
        for record in event["Records"]:
            message = json.loads(record["body"])

            print(f"Procesando mensaje: {message['message_id']}")

            with connection.cursor() as cursor:
                sql = "UPDATE messages SET processed = 1 WHERE message_id = %s"
                cursor.execute(sql, (message["message_id"],))
            connection.commit()
    finally:
        connection.close()

    return {"statusCode": 200, "body": "Worker execution complete"}
