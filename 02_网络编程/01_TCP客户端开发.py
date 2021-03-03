# 李禄波
# 2021/2/6 16:01

import socket


# 1.创建客户端套接字对象
# 参数1：socket.AG_INET 代表ipv4（IP协议的版本）
# 参数2：socket.SOCK_STREAM 代表TCP协议（通讯控制协议）
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.和服务端套接字建立连接
# 参数：元组（有两个元素的元组）
# 元素1：服务器IP地址（字符串类型）
# 元素2：服务器端口号（整型）
tcp_client_socket.connect(("192.168.146.133", 8080))

# 3.发送数据
# 发送数据时需先将数据转换成二进制格式
tcp_client_socket.send("我是眉下即是远山".encode("utf-8"))

# 4.接收数据
# 参数是以字节为单位的接收数据大小
# recv会阻塞等待数据的到来
recv_data = tcp_client_socket.recv(1024)
recv_data = recv_data.decode("utf-8")
print(recv_data)

# 5.关闭客户端套接字
tcp_client_socket.close()
