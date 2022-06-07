import socket
import time

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

#127.0.0.0 代表本机所有ip
#127.0.0.1 本地回环地址

ipaddr = ('127.0.0.1',9995)
server.bind(ipaddr)
#bind之后，要listen,看是否有来建立连接的

#Linux命令：ss   Socket Statistics  
#cmd命令 netstat

#listen之后才会占用端口
server.listen()

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

s1,raddr = server.accept()
#等待对方连过来
#有连接就会给客户端分配一个新socket，用上面占用的端口
#为了不阻塞server这个socket，会返回一个新的socket对象和对端地址

#以下三句可以循环
data = s1.recv(1024)
#receive up to buffersize bytes from the socket
#在s1上等，但是server的socket还在监听
print(data)
#
s1.send('ack. {}'.format(data.decode()).encode())


s1.close()
server.close()
