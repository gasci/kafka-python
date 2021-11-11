from json import dumps
from kafka import KafkaProducer
from time import sleep


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

while True:
    val = input("")
    sleep(0.1)
    producer.send('raw', value=val)
