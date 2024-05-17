import pika, json
import os
import environ

env = environ.Env()
environ.Env.read_env()

rabbitmq_url=env('rabbitmq_url')

params = pika.URLParameters(rabbitmq_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)