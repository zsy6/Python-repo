from http import client
import importlib
from itertools import count
from pydoc import cli
import socket
import sys


def create_client(ipaddr,port):
    client = socket.socket()

    count_fail = 0 

    #直到连接
    while True:
        try:
            client.connect((ipaddr,port))
            break
        except socket.error:
            count_fail += 1
            print("fail to connect to server %d times" %count_fail)
            if count_fail == 3:
                print("连接失败")
                exit(-1)
                
            

    count_send = 0
    count_recv = 0
    while True:
        count_send += 1
        msg = "hello,I am client."+"This is "+str(count_send)+" send"
        client.send(msg.encode('utf-8'))
        msg_recv = client.recv(1024)
        count_recv += 1
        print(msg_recv.decode('utf-8'))
        print("这是client接收到的第"+str(count_recv)+"条消息")
        if count_recv == 10:
            msg = "disconnect"
            print("client主动断开连接")
            client.send(msg.encode('utf-8'))
            break
        
    client.close()


if __name__ == '__main__':
    create_client('127.0.0.1',9995)