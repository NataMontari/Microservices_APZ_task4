from flask import Flask, request, jsonify
import sys
from kafka import KafkaConsumer
import json

app = Flask(__name__)

received_messages = [""]

consumer = KafkaConsumer(
    'messages',
    bootstrap_servers= ['localhost:9092', 'localhost:9093'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='messages-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    # try:
    while True:
            # Explicitly poll messages
        msg_pack = consumer.poll(timeout_ms=1000)
        print(msg_pack)
        if msg_pack:
            for topic_partition, messages in msg_pack.items():
                for message in messages:
                    print(f"Consumed message: {message.value}")
                    received_messages.append(message.value)
        if msg_pack == {}:
            break
        


    # except Exception as e:
    #     print(f"Error consuming messages: {e}")


    return 0

@app.route("/get_message", methods=["GET"])
def get_message():
    consume_messages()
    return jsonify({
        "port": port,
        "messages": received_messages
    }), 200


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("Please enter a port number from 8082 to 8084")
    port = int(sys.argv[1])  # Перетворюємо на int
    if port < 8085 or port > 8089:
       raise Exception("Please enter a port number from 8082 to 8084")
    
    print(f"Running messages-service on port {port}")
    app.run(port=port)
