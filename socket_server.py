import socket

# 建立一个服务端
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.6', 8002))  # 绑定要监听的端口
# server.accept()
server.listen(5)  # 开始监听 表示可以使用五个链接排队
while True:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
    # print(conn, addr)
    print("已链接",addr)
    data = conn.recv(100)
    # print('1接受到数据:', data.decode())  # 打印接收到的数据
    # print(addr)
    while data:
        try:
            # data = conn.recv(100)  # 接收数据
            print('2接受到数据:', data.decode())  # 打印接收到的数据
            data = conn.recv(100)  # 接收数据
        except ConnectionResetError as e:
            print('关闭了正在占线的链接！')
            # break
        # break
    break
conn.close()

