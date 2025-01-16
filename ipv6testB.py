import socket

# 定义IPv6地址和端口
HOST = '2409:8a30:b486:73d0:a019:254f:5e90:7c5a'  # 服务器的IPv6地址
PORT = 12345  # 服务器监听的端口号

# 创建IPv6 TCP socket
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"连接到 {HOST}:{PORT}...")

# 只发送数据
try:
    while True:
        message = input("请输入发送消息: ")
        client_socket.sendall(message.encode())  # 发送消息
except KeyboardInterrupt:
    print("客户端关闭。")
finally:
    client_socket.close()
