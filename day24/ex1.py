"""
- 创建客户端套接字对象
- 和服务端套接字建立连接
- 发送数据
- 接收数据
- 关闭客户端套接字

"""

"""
family : 表示ip地址类型，分为IPv4和IPv6
type：表示传输协议

connect((host, port)) 表示和服务端套接字建立连接，host是服务器ip地址,port是端口号

send(data)  表示发送数据,data是二进制数据

recv(buffersize)表示接收数据，buffersize是每次接收数据的长度
"""

import socket

# 创建客户端套接字对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 客户端程序不强制要求绑定端口号
# tcp_client_socket.bind(("", 8091))

# 和服务端套接字建立连接
tcp_client_socket.connect(("192.168.31.59", 9091))


send_data = "你好，我是享学课堂客户端"
send_content = send_data.encode("gbk")
# 发送数据
tcp_client_socket.send(send_content)

# 接收数据
# 1024 表示每一次接收的最大字节数
recv_data = tcp_client_socket.recv(1024)

# 对二进制数据进行解码
recv_content = recv_data.decode("gbk")
print("接收到服务端的数据为:", recv_content)

# 关闭套接字
tcp_client_socket.close()

# 在windows里面把编码格式转换为GBK，正常和网络调试助手发送和接收数据
# 在windows里面把编码格式转换为utf-8，正常和网络调试助手发送和接收数据