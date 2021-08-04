# -*- coding: UTF-8 -*- 

import socket
import time
BUFSIZE = 1024
local_ip_port = ('192.168.1.1', 8002)
remote_ip_port = ('192.168.1.10', 4002)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
server.bind(local_ip_port)

senddata = b"\x08\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00"
server.sendto(senddata,remote_ip_port)
print(remote_ip_port)


while True:
    data,client_addr = server.recvfrom(BUFSIZE)
    print('->server收到的数据:', data.hex())

#     server.sendto(senddata,remote_ip_port)
#     print('<-发送数据:', senddata)
 
server.close()

if __name__ == "__main__":
    pass
    