from kafka import KafkaProducer, KafkaConsumer
from json import loads, dumps
from time import sleep
from settings import GROUP_ID, BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    'raw',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id=GROUP_ID,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

array = []

for event in consumer:
    event_data = event.value
    print(f"raw: {event_data}")
    array.append(event_data)
    
    # reset the array if empty
    # if event_data == "":
    #     array.clear()
    # sleep(0.1)
    producer.send('array', value=array)
