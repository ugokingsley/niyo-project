import pika, json
import os
import environ

env = environ.Env()
environ.Env.read_env()

rabbitmq_url=env('rabbitmq_url')

params = pika.URLParameters(rabbitmq_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

# This method will be called inside view for sending RabbitMQ message
# reports an event to the queue of streams
# routing key here must match the queue name in the consumer
def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)


