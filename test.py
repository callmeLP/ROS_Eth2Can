# -*- coding: UTF-8 -*- 

from iVista import *
import threading

def callback():
    print("1")

class sendThread(threading.Thread): 
    def __init__(self, server):
        threading.Thread.__init__(self)
        self.server = server

    def run(self):
        self.server.canSend()

class recThread(threading.Thread): 
    def __init__(self, server):
        threading.Thread.__init__(self)
        self.server = server

    def run(self):
        self.server.recvfrom_exe(1024,callback)


if __name__ == "__main__":
    server = iVistaCan(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    send = sendThread(server)
    rec = recThread(server)

    send.start()
    rec.start()

    send.join()
    rec.join()


    # time.sleep(3)
    # server.canChangeSendData("Gear_Shift_Cmd", b"\x11\x22\x33\x44\x00\x00\x00\x00")
    # print('1')
    