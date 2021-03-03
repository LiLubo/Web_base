
# 李禄波
# 2021/2/6 17:44

import socket

# 1.创建服务端套接字对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置端口复用（作用：一旦客户端关闭端口立马释放）
# 参数：
# 参数1：socket.SOL_SOCKET 设置socket选项
# 参数2：socket.SO_REUSEADDR 地址复用
# 参数3：True：代表开启选项 False：代表不开启（默认不开启）
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 2.绑定端口号
# 参数：元组（有两个元素）
# 元素1：IP地址（字符串）此处可填写真实IP/不写/127.0.0.1都是指代本机IP地址
# 元素2：端口号（整型）
tcp_server_socket.bind(("192.168.146.1", 8080))

# 3.设置监听
# 参数是最大监听个数（排队客户端的最大等待个数）
# 此时tcp_server_socket就会从主动套接字变成被动套接字（不能发送数据）
# 该tcp_server_socket只用于接受连接请求
tcp_server_socket.listen(128)

# 4.等待接受客户端的连接请求
# <返回值> 是一个元组（有两个元素）
# 元素1：和客户端进行通信的socket
# 元素2：客户端的地址信息（IP地址、端口号）
# client_socket负责处理连接请求（可接受数据，也可发送数据）
client_socket, client_addr = tcp_server_socket.accept()
print("client_socket:", client_socket)
print("client_addr:", client_addr)

# 5.接收数据
# 参数是接收数据的大小（字节）
recv_data = client_socket.recv(1024)
recv_data = recv_data.decode("utf-8")
print(recv_data)

# 6.发送数据
client_socket.send("hello win7".encode("utf-8"))

# 7.关闭套接字
# 先关闭处理连接请求的socket,再关闭接收连接请求的socket
client_socket.close()
tcp_server_socket.close()
