# Import librairies
import socket
from random_values import values
from time import *
import json
from router import add_infos


class Py_socket:

    def __init__(self,id,frequency):
        self.id = id
        self.li = []
        self.frequency = frequency
        self.s = socket.socket()
        self.s.connect(('127.0.0.1',8080))

    def receive_data(self) :
        # Creation of empty array to stock data
        result = values(self.li,self.id)
        add_infos(self.li[0],self.li[1],self.li[2],self.li[3],self.li[4],self.li[5],self.li[6],self.li[7],self.li[8],self.li[9])
        return result

    def create_file(self) :
        timestamp = int(time.time())
        filename = "paramunite_" + str(self.id) + "_" + str(timestamp) + ".json"
        f = open(filename, "a")
        f.write()
        f.close()


    def convert_data(data) :
        json_dump = json.dumps(data)
        # Cast the array to string to send bytes
        request = bytes(json_dump, 'utf-8')
        return request

    def send_data(self,req) :
        self.s.send(req)
        sleep(self.frequency)

py_socket = Py_socket()


