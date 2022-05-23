import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect(('192.168.31.59', 8082))

send_data = '你好，我是客户端2'
send_content = send_data.encode('gbk')
tcp_client_socket.send(send_content)

recv_data = tcp_client_socket.recv(1024)
recv_content = recv_data.decode('gbk')

print('客户端2接收到服务器端的数据为：', recv_content)

tcp_client_socket.close()