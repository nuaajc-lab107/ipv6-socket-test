import socket

# 定义IPv6地址和端口
HOST = '::'  # 绑定到所有IPv6地址
PORT = 12345  # 任意选择的端口号

# 创建IPv6 TCP socket
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"服务器在 {HOST}:{PORT} 等待连接...")

# 等待客户端连接
conn, addr = server_socket.accept()
print(f"连接来自 {addr}")

# 只接收数据
try:
    while True:
        data = conn.recv(1024)  # 接收客户端发送的消息
        if not data:
            print("客户端关闭了连接")
            break  # 如果没有数据，表示客户端关闭了连接

        print(f"收到消息: {data.decode()}")  # 打印收到的消息
except KeyboardInterrupt:
    print("服务器关闭。")
finally:
    conn.close()
    server_socket.close()
