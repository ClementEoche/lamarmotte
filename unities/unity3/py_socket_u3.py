# Import librairies
import socket
from scripts.random_values import values
from time import *
import json
import requests


class Py_socket:

    def __init__(self,frequency):
        self.id = 3
        self.li = []
        self.frequency = frequency
        self.s = socket.socket()
        self.s.connect(('127.0.0.1',8080))

    def receive_data(self) :
        # Creation of empty array to stock data
        result = values(self.li,self.id)
        return result

    def create_file(self) :
        timestamp = int(time.time())
        filename = "paramunite_" + str(self.id) + "_" + str(timestamp) + ".json"
        f = open(filename, "a")
        f.write()
        f.close()


    def convert_data(data) :
        req = json.dumps(data)
        return req

    def send_data(self,req) :
        r = requests.post('http://localhost/nomdeprojet/collectors/collectorunity/collector/info', json=req)
        sleep(self.frequency)

py_socket = Py_socket(5)

while True:
    array_data = py_socket.receive_data()
    py_socket.create_file()
    json_data = py_socket.convert_data(array_data)
    py_socket.send_data(json_data)