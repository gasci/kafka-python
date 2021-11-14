from kafka import KafkaConsumer
from json import loads
from time import sleep

from settings import GROUP_ID, BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    'array',
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id=GROUP_ID,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for event in consumer:
    event_data = event.value
    # sleep(0.1)
    print(f"array: {event_data}")
