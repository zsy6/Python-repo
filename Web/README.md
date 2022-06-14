## 服务器端

1. 创建socket对象
2. 绑定ip地址 端口
3. listen()
4. accept()阻塞等待客户端建立连接   accept一旦连接会建立新的一个socket，返回新的socket对象、对端地址
新的socket对象里有：fd、localaddr、remoteaddr

5. 缓冲区接收数据 recv(bufsize[,flags])
6. 发送数据 send(bytes)
7. close() 可以把文件描述符还回去

### 阻塞状态
accept、recv、send都是阻塞的
需要用多线程实现非阻塞

