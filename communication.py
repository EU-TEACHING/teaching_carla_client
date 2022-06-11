import pika
from  datetime import datetime, timedelta
import json
import threading

class Teaching_Transceiver():
    def __init__(self,host='localhost',port=5672,username='teaching',password='asd123456'):
        credentials = pika.PlainCredentials(username, password)
        parameters = pika.ConnectionParameters(host,port,'/',credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.connection2= pika.BlockingConnection(parameters)

        self.channel = self.connection.channel()
        self.channel2 = self.connection2.channel()
        self.channel2.queue_declare(queue='rl.queue')
        self.channel2.queue_bind(exchange='amq.topic',
                   queue='rl.queue',
                   routing_key='prediction.driving_profile.value')
        self.channel2.basic_consume(queue='rl.queue',
                      auto_ack=True,
                      on_message_callback=self.callback)
        self.prediction = 1
        self.consumer_service = threading.Thread(target=self.star_consumer,daemon=True)
        self.consumer_service.start()

                    
    def star_consumer(self):
         self.channel2.start_consuming()

    def publish(self,message):

        packet = {"service_type": "carla.transmiter",
                    "service_name": "cs",
                    "topic": "sensor.carla.value", "timestamp": (datetime.now()-timedelta(days = 2)).isoformat(),
                    "body": message}

        self.channel.basic_publish(exchange='amq.topic',
                      routing_key='sensor.carla.value',
                      body=json.dumps(packet, default=str))


    def callback(self,ch, method, properties, body):
        self.prediction = json.loads(body)['body']['driving_profile']
        print(f'New prediction {self.prediction}')


    def __del__(self):   
        self.connection.close()   
        self.channel2.queue_delete(queue='rl.queue')  
        self.connection2.close()