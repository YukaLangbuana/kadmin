from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import kafka
import os
import json

@api_view(['POST'])
def send_topic(request):
    topic_name = request.data['topic_name']
    topic_message = request.data['message']
    producer = kafka.KafkaProducer(bootstrap_servers=[f"{os.environ['KAFKA_HOST']}:{os.environ['KAFKA_PORT']}"])
    producer.send(topic_name, topic_message.encode('utf-8'))
    return Response(data={"topic_name": topic_name, "message": topic_message}, status=status.HTTP_200_OK)

@api_view(['GET'])
def sample_topic(request, topic_name):
    consumer = kafka.KafkaConsumer(
        topic_name, 
        bootstrap_servers=[f"{os.environ['KAFKA_HOST']}:{os.environ['KAFKA_PORT']}"],
        enable_auto_commit=False,
        auto_offset_reset='earliest',
    )
    res = consumer.poll(timeout_ms=1000)
    for _, v in res.items():
        print(v[-1].value.decode('utf-8'))
        return Response(data={"message": v[-1].value.decode('utf-8')}, status=status.HTTP_200_OK)
    return Response(data={"message": "No message"}, status=status.HTTP_200_OK)
