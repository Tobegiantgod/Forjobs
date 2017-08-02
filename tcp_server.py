#coding: utf-8

import socket
import threading

#注意port为整数，不是字符串

bind_ip = "0.0.0.0"
bing_port = 9999


#tcp_server
def tcp_server(bind_ip, bind_port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((bind_ip, bind_port))

    server.listen(5)

    print("[*]Listening on {}:{}".format(bind_ip, bing_port))

    #处理客户线程
    def handle_client(client_socket):

        request = client_socket.recv(1024)

        print("[*] Received: {}".format(request.decode('utf-8')))

        client_socket.send(b"ACK!")

        client_socket.close()

    #进入监听主循环
    while True:
        client, addr = server.accept()

        print("[*] Accepted connection from {}:{}".format(addr[0],addr[1]))

        #挂起客户端线程，处理传入数据
        client_handler = threading.Thread(target=handle_client, args=(client,))

        client_handler.start()





if __name__ == '__main__':

    tcp_server(bind_ip, bing_port)





