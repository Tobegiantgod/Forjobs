#coding: utf-8

import socket

target_host = "www.baidu.com"
target_port = 80

#udp_client
def udp_client(target_host, target_port):

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.sendto(b"you are best!", (target_host, target_port))

    data, addr = client.recvfrom(4096)

    print("receive from {}".format(addr.decode('utf-8')))

    print(data.decode('utf-8'))

if __name__ == '__main__':

    udp_client()