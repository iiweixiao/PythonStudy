import socket  # for sockets
import sys  # for exit

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket. Error'
          ' code: ')
    sys.exit()

print('Socket Created')

host = 'www.oschina.net'
port = 80  # http协议，网页访问

try:
    remote_ip = socket.gethostbyname(host)  # 获取网址的ip地址

except socket.gaierror:
    # could not resolve
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)

# Connect to remote server
s.connect((remote_ip, port))  # 远程到目标网址服务器

print('Socket Connected to ' + host + ' on ip ' + remote_ip)

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try :
    # Set the whole string
    s.sendall(message.encode('utf-8'))
except socket.error:
    # Send failed
    print('Send failed')
    sys.exit()

print('Message send successfully')

reply = s.recv(4096)
print(reply.decode('utf-8'))

s.close()