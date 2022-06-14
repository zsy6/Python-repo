import socket
import threading
#多线程import logging可以看它在不同线程里跑
import logging 


class ChatSever:
    def __init__(self,ipadd='127.0.0.1',port=9995):
        self.server_addr = (ipadd,port)
        self.server_socket = socket.socket()
        

    def start(self):
        self.server_socket.bind(self.server_addr)
        self.server_socket.listen()


    def stop(self):
        pass