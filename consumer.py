from confluent_kafka import Consumer, KafkaError
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json

# Kafka consumer
c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'temp-group',
    'auto.offset.reset': 'earliest'
})
c.subscribe(['temperature'])

# InfluxDB client
client = InfluxDBClient(
    url='http://influxdb:8086',
    token='admin123',
    org='my-org'
)
write_api = client.write_api(write_options=SYNCHRONOUS)
bucket = 'temperature'

print("Waiting for messages...")

try:
    while True:
        m = c.poll(1.0)
        if m is None: 
            continue
        if m.error():
            if m.error().code() != KafkaError._PARTITION_EOF:
                print(f"Error: {m.error()}")
            continue
        
        try:
            # Attempt to parse message as JSON
            data = json.loads(m.value())

            # Validate required fields in the message
            if all(key in data for key in ['sensor_id', 'timestamp', 'temperature']):
                point = (
                    Point("temperature")
                    .tag("sensor_id", data['sensor_id'])
                    .field("value", data['temperature'])
                    .time(int(data['timestamp'] * 1e9))
                )
                write_api.write(bucket=bucket, org='my-org', record=point)
                print(f"Written to InfluxDB: {data}")
            else:
                print(f"Invalid message format: {data}")

        except (json.JSONDecodeError, TypeError) as e:
            print(f"Failed to parse message: {m.value()} - {e}")

except KeyboardInterrupt:
    print("Consumer stopped.")

finally:
    c.close()