import time
import random
import paho.mqtt.client as mqtt

broker_address = "hivemq"
port = 1883
topic = "dados/simulador"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt.Client("Simulador")
client.on_connect = on_connect
client.connect(broker_address, port=port)

while True:
    temperatura = random.uniform(20.0, 30.0)
    umidade = random.uniform(40.0, 60.0)
    mensagem = f'{temperatura},{umidade}'
    client.publish(topic, mensagem)
    print(f"Publicado: {mensagem} no tópico {topic}")
    time.sleep(5)