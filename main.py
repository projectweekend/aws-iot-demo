import os
import paho.mqtt.client as paho


IOT_CA_ROOT = '/home/pi/iotkeys/rootCA.pem'
IOT_CERT = '/home/pi/iotkeys/cert.pem'
IOT_KEY = '/home/pi/iotkeys/privateKey.pem'
IOT_URL = os.getenv('IOT_URL')
assert IOT_URL


def on_message(client, userdata, message):
    print(message.topic)
    print(str(message.payload))


def main():
    client = paho.Client()
    client.on_message = on_message
    client.tls_set(ca_certs=IOT_CA_ROOT, certfile=IOT_CERT, keyfile=IOT_KEY, tls_version=4)
    client.connect(IOT_URL, 8883)
    client.subscribe('whatever')
    client.loop_forever()


if __name__ == "__main__":
    main()
