import paho.mqtt.client as mqtt
import pymongo
import ssl
import pymongo
import time
import re

HOST = "ptnetsuite.a2asmartcity.io"
PORT = 8883
client_id = "dellanna::test_wang"
localtime = time.asctime(time.localtime(time.time()))
realtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/sub/v1/users/dellanna/apps/9901/devices/0004a30b001ac249/uplink/+")


def on_message(client, userdata, msg):
    string = str(msg.payload)
    p1 = re.compile(r'["](.*?)["]', re.S)
    need = re.findall(p1, string)
    a = need[1]
    al = []
    s = ''
    for i in range(0, len(a), 2):
        b = a[i:i + 2]
        al.append(chr(int(b, 16)))
    realneed = s.join(al)
    print(realneed)
    print("message:" + realneed)
    dict = {"time": realtime, "payload": realneed}
    print(dict)
    result = collection.insert(dict)
    print(result)
    p2 = re.compile(r'[:](.*?)[,]', re.S)
    seperate = re.findall(p2, s)
    temperature = seperate[0]
    humidity = seperate[1]
    PM1 = seperate[2]
    PM2_5 = seperate[3]
    PM10 = seperate[4]
    a = seperate[5]
    b = seperate[6]
    print(temperature)
    print(humidity)
    print(PM1)
    print(PM2_5)
    print(PM10)
    print(latitude)
    print(longtitude)
    txt = ["time: " + str(realtime) + ", temperature: " + str(temperature) + ", humidity: " + str(humidity) + ", PM1.0: " + str(PM1) + ", PM2.5: " + str(PM2_5) + ", PM10: " + str(PM10)]
    gmap1 = gmplot.GoogleMapPlotter(45.47879, 9.230597, 13 )
    gmap1.marker( latitude, longitude, title = txt)
    gmap1.apikey = "AIzaSyAxJvQZ7hX8F3Ojn886w52rxVgneCiB2gA"
    gmap1.draw( "/Users/sephiros/Desktop/program/visualization.html" )

def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)


mgclient = pymongo.MongoClient(host='localhost', port=27017)
db = mgclient.thesis
collection = db.mqtt_payload

client = mqtt.Client(client_id)
client.username_pw_set("dellanna", "t3ll1n4p0c")
client.tls_set("/Users/sephiros/Desktop/ptNetSuite_mqtt_ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 60)
client.loop_forever()
