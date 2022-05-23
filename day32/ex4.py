import socket
import threading
import  framework

class HttpWebServer(object):
    def __init__(self):
        tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSWADDR, True)
        tcp_sever_socket.bind(("", 8080))

        tcp_sever_socket.listen(128)
        self.tcp_dever_socket = tcp_sever_socket

    @staticmethod
    def handle_client_request(new_socket):
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return

        recv_content = recv_data.decode('utf-8')
        print(recv_content)

        request_list = recv_content.split(" ", maxsplit =2)

        request_path = request_list[1]
        print(request_path)


        if request_path == '/':
            request_path = '/index.html'

        if request_path.endswith(".html"):
            env = {
                "request_path": request_path
            }

            status, headers, response_body = framwork.handle_request(env)
            print(status, headers, response_body)

        response_line = "HTTP/1.1 %s\r\n" % status

        response_header = ""
        for header in headers:
            response_header += "%s: %s\r\n" % header

        response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")

        new_socket.send(response_data)
        new_socket.close()

def start(self):
    while True:
        new_socket, ip_port = self.tcp_dever_socket.accept()
        threading.Thread(target=self.handle_client_request, args=(new_socket,))
        sub_thread.setDaemon(True)
