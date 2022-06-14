from base64 import encode
import importlib
from itertools import count
import socket
import time
import sys

def create_server(ipaddr,port):
    server = socket.socket()
    print(server)
    '''
    <socket.socket fd=800, 
    family=AddressFamily.AF_INET, 
    type=SocketKind.SOCK_STREAM, 
    proto=0>
    '''
    #协议家族IPv4 AF_INET
    #Socket类型 IPv6  SOCK_STREAM
    print(server.bind)

    server.bind((ipaddr,port))
    #bind之后，要listen,看是否有来建立连接的

    #Linux命令：ss   Socket Statistics  
    #cmd命令 netstat

    try:
    #listen之后才会占用端口
        server.listen()
    except socket.error:
        print("fail to listen")
        sys.exit(-1)
        
    #time.sleep(5)
    
    '''
    用time.sleep(5)
    再通过系统cmd查看
    确实有127.0.0.1:9995的监听进程
    需要在程序中保留这个状态
    '''

    print(id(server))
    #打印server的地址
    print(server)

    while True:
        print("waiting for connection...")
        try:
            s1,raddr = server.accept()
            #等待对方连过来
            #有连接就会给客户端分配一个新socket，用上面占用的端口
            #为了不阻塞server这个socket，会返回一个新的socket对象和对端地址
            break
        except:
            print("fail to connect")
            sys.exit(-1)

    while True:
        #loop until client desconnect
        try:
            msg = s1.recv(1024)
        #receive up to buffersize bytes from the socket
        #在s1上等，但是server的socket还在监听
        #print(msg)
        except socket.error:
            print('no recv')
            sys.exit(-1)

        msg_de = msg.decode('utf-8')
        print(msg_de)
        if msg_de == 'disconnect':
            print("Client disconnect active connection")
            s1.close()
            server.close()
            break

        #s1.send('ack. {}'.format(msg.decode().encode()))
        #TypeError: a bytes-like object is required, not 'str'
        s1.send(('ack. {}'.format(msg)).encode('utf-8'))


if __name__ == '__main__':
    create_server('127.0.0.1',9995)
    #127.0.0.0 代表本机所有ip
    #127.0.0.1 本地回环地址
