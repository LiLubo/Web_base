# 李禄波
# 2021/2/7 18:53

import socket


def handler_client_request(client_socket):

    """
    和浏览器进行交互的函数
    :param client_socket: 处理浏览器和服务器之间的交互
    :return:
    """
    # 接收数据
    recv_data = client_socket.recv(1000000)

    # 客户端关闭
    if len(recv_data) == 0:
        return

    recv_data = recv_data.decode("utf8")
    print(recv_data)

    # 对请求报文按空格进行切割
    path_list = recv_data.split(" ")

    # 请求资源路径
    request_path = path_list[1]

    try:
        # 打开文件
        f = open("./static" + request_path, 'rb')
        # file_data 存放着图片资源
        file_data = f.read()
        f.close()

    except Exception as e:
        # 浏览器访问的网址里的资源不存在
        print("异常信息：", e)
        # 访问不成功的应答报文
        response_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header = "server:py1.0\r\n"
        response_body = "SORRY，NOT FOUND"

        # 将相应信息发送给浏览器
        response_data = response_line + response_header + '\r\n' + response_body
        client_socket.send(response_data.encode())

        client_socket.close()
    else:
        # 浏览器要访问的资源存在
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


def main():

    """
    控制整个服务器流程的函数
        tcp_server_socket:用来接收连接的socket
        client_socket:用来处理和浏览器之间的数据交互
    """

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

        if not handler_client_request(client_socket):
            break

    tcp_server_socket.close()


if __name__ == '__main__':
    main()

