#coding: utf-8

import socket


#注意port为整数，不是字符串

target_host = "www.baidu.com"
target_port = 80

#tcp_client
def tcp_client(target_host, target_port):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host,target_port))

    client.send(b"GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

    response = client.recv(4096)

    print(response.decode('utf-8'))

if __name__ == '__main__':

    tcp_client("127.0.0.1", 9999)
