import time
import random
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

# Define the Avro Schema (V3)
value_schema_str = """
{
  "namespace": "com.sensor.data",
  "type": "record",
  "name": "SensorReading",
  "fields": [
    {"name": "sensor_id", "type": "string"},
    {"name": "temperature", "type": "float"},
    {"name": "status", "type": "string"}
  ]
}
"""
value_schema = avro.loads(value_schema_str)

# Configuration for K8s Tunnels
conf = {
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081'
}

producer = AvroProducer(conf, default_value_schema=value_schema)

print("📡 [K8s Producer] Sending sensor data...")

try:
    while True:
        data = {
            "sensor_id": f"SENSOR-{random.randint(1, 50)}",
            "temperature": round(random.uniform(18.0, 45.0), 2),
            "status": "ACTIVE"
        }
        producer.produce(topic='sensor_data_v3', value=data)
        producer.flush()
        print(f"✅ Data Sent: {data}")
        time.sleep(1.5)
except KeyboardInterrupt:
    print("Producer stopped.")