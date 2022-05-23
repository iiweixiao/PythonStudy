import socket
import threading
import time


def handle_client_request(ip_port, new_client):
    print('客户端ip和端口号分别为：', ip_port)

    while True:
        recv_data = new_client.recv(1024)
        if recv_data:
            print('接收的数据长度是：', len(recv_data))
            recv_content = recv_data.decode('gbk')

            send_content = '我服务器，已收到你客户端的请求'
            send_data = send_content.encode('gbk')
            new_client.send(send_data)
        else:
            print('客户端已经下限了：', ip_port)
    new_client.close()


def main():
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_sever_socket.bind(('', 8082))

    tcp_sever_socket.listen(128)

    while True:
        new_client, ip_port = tcp_sever_socket.accept()

        tcp_thread = threading.Thread(target=handle_client_request, args=(ip_port, new_client))

        tcp_thread.Daemon = True
        tcp_thread.start()

        time.sleep(1)


if __name__ == '__main__':
    main()