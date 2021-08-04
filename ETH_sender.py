# -*- coding: UTF-8 -*- 
import time
import socket
BUFSIZE = 1024

remote_ip_port = ('192.168.1.10', 4001)

def initSocket():
    local_ip_port = ('192.168.1.1', 8001)
    remote_ip_port = ('192.168.1.10', 4001)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
    server.bind(local_ip_port)
    return server


# while True:
#     data,client_addr = server.recvfrom(BUFSIZE)
#     print('server收到的数据', data.hex())
#     print(client_addr)
 
# server.close()

if __name__ == "__main__":
    server =initSocket()

    while True:
        data = "\x08\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00"
        data = bytes(data, "utf-8")
        server.sendto(data ,remote_ip_port)
        time.sleep(0.02)
        break
