import pika
from kafka3 import KafkaConsumer

consumer = KafkaConsumer("datascience")
for record in consumer:
    message = record.value.decode("utf-8")
    print(f"Got message: {message}")

QUEUE_NAME = "mailbox"

def callback(channel, method, properties, body):
    message = body.decode("utf-8")
    print(f"Got message: {message}")

with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_consume(
        queue=QUEUE_NAME,
        auto_ack=True,
        on_message_callback=callback
    )
    channel.start_consuming()