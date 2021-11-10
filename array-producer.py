from kafka import KafkaProducer, KafkaConsumer
from json import loads, dumps


consumer = KafkaConsumer(
    'raw',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

array = []

for event in consumer:
    event_data = event.value
    print(f"raw: {event_data}")
    array.append(event_data)
    
    # reset the array if empty
    if event_data == "":
        array.clear()
    producer.send('array', value=array)
