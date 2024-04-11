import os
import paho.mqtt.client as mqtt
import psycopg2

broker_address = "hivemq"
port = 1883
topic = "dados/simulador"

db_name = os.getenv('POSTGRES_DB', 'postgres')
db_user = os.getenv('POSTGRES_USER', 'postgres')
db_password = os.getenv('POSTGRES_PASSWORD', 'postgres')
db_host = 'db'

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    temperatura, umidade = msg.split(',')
    
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO medicoes (temperatura, umidade) VALUES (%s, %s);", (temperatura, umidade))
    conn.commit()
    cur.close()
    conn.close()

client = mqtt.Client("Processador")
client.connect(broker_address, port=port)
client.subscribe(topic)
client.on_message = on_message

client.loop_forever()