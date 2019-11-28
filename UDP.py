# 不需要建立连接
import socket
# 创建socket对象
# SOCK_DGRAM    udp模式
send1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送数据 字节
send1.sendto("什么是socket？".encode(), ("172.16.158.28", 8000))

# 创建socket对象
# SOCK_DGRAM  udp模式
receive1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive1.bind(("172.16.158.28", 8000))  # 绑定服务器的ip和端口
data = receive1.recv(1024)  # 一次接收1024字节
print(data.decode())  # decode()解码收到的字节


