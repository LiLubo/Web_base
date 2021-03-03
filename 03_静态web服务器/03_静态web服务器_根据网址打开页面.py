# 李禄波
# 2021/2/7 16:31


import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 绑定地址
tcp_server_socket.bind(("127.0.0.1", 8080))

# 设置监听
tcp_server_socket.listen(128)

while True:

    # 接受连接请求
    client_socket, client_addr = tcp_server_socket.accept()

    # 接收数据
    recv_data = client_socket.recv(1000000)

    # 客户端关闭
    if len(recv_data) == 0:
        break

    recv_data = recv_data.decode("utf8")
    print(recv_data)

    # 对请求报文按空格进行切割
    path_list = recv_data.split(" ")

    # 请求资源路径
    request_path = path_list[1]
    print("request:", request_path)

    # 打开文件
    f = open("./static" + request_path, 'rb')
    # file_data 存放着图片资源
    file_data = f.read()
    f.close()

    # 发送数据
    # 应答行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 应答头
    response_header = "server:py1.0\r\n"
    # 应答体
    response_body = file_data
    response_data = (response_line + response_header + '\r\n').encode() + response_body

    client_socket.send(response_data)
    client_socket.close()


tcp_server_socket.close()

