
import socket  # 客户端 发送一个数据，再接收一个数据

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明socket类型，同时生成链接对象
client.connect(('192.168.1.4', 8002))  # 建立一个链接，连接到本地的6969端口

while True:
    msg = input('输入：')  # strip默认取出字符串的头尾空格
    if msg != 'exit':
        client.send(msg.encode('utf-8'))  # 发送一条信息 python3 只接收btye流
    else:
        print(ConnectionError)
        client.send('客户说我走了，输入了exit，然后就关闭了链接'.encode('utf-8'))
        client.close()
        break

