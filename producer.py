from confluent_kafka import Producer
import time, random, json

p = Producer({'bootstrap.servers': 'kafka:9092'})
topic = 'temperature'

def gen_temp():
    return round(random.uniform(20.0, 30.0), 2)

try:
    while True:
        msg = {
            'sensor_id': 'sensor-1',
            'timestamp': time.time(),
            'temperature': gen_temp()
        }

        # Validate message before sending
        if all(key in msg for key in ['sensor_id', 'timestamp', 'temperature']):
            p.produce(topic, json.dumps(msg).encode('utf-8'))
            p.flush()
            print(f"Produced message: {msg}")
        else:
            print(f"Invalid message skipped: {msg}")
        
        time.sleep(5)

except KeyboardInterrupt:
    print("Producer stopped.")