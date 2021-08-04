# -*- coding: UTF-8 -*- 
import socket
import time

class iVistaCan(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
        socket.socket.__init__(self, family, type, proto, fileno)
        self.local_addr = ('192.168.1.1', 8001)    #本机地址
        self.remote_addr = ('192.168.1.10', 4001)     #以太网转can地址
        self.bind(self.local_addr)
        self.__canLen = b"\x08"
        self.__canCtrlIdPool = {    #控制id池(私有)
            "Gear_Shift_Cmd":b"\x00\x00\x00\xA1",
            "Steering_Control_Cmd":b"\x00\x00\x00\xA2",
            "Drive_Control_Cmd":b"\x00\x00\x00\xA3",
            "Brake_Control_Cmd":b"\x00\x00\x00\xA4",
            "Parking_Cmd":b"\x00\x00\x00\xA5" 
        }  
        self.canCtrlDataPool = {    #控制指令池
            "Gear_Shift_Cmd":b"\x00\x00\x00\x00\x00\x00\x00\x00",
            "Steering_Control_Cmd":b"\x00\x00\x00\x00\x00\x00\x00\x00",
            "Drive_Control_Cmd":b"\x00\x00\x00\x00\x00\x00\x00\x00",
            "Brake_Control_Cmd":b"\x00\x00\x00\x00\x00\x00\x00\x00",
            "Parking_Cmd":b"\x00\x00\x00\x00\x00\x00\x00\x00"
        }   

    def __recvCallBack(self, data):
        '''
        接收信号的回调函数:（暂时只识别VCU_FeedBack的数据 id：0xC1）
            在recvfrom_exe()中注册
            data为以太网发来的can数据
        '''
        if data[4] == 193:          #第五个字节是0xc1
            print(data[5], data[6])
            temp = data[5]*(2**8)+data[6]
            vel = temp/100
            print("速度:"+ str(vel) + "km/h")

    def recvfrom_exe(self, bufsize):
        '''
        以太网接收:
            写在单独的线程中
            bufsize：buff的大小
            callbak:收到数据后的回调
        '''
        while True:
            data,client_addr = self.recvfrom(bufsize)
            print(data.hex() , client_addr)
            self.__recvCallBack(data)
            # return data,client_addr


    def canSend(self):
        '''
        以太网发送:
            20ms一帧 循环发送A1到A5（需要写在单独线程中）
        '''
        while True:
            for i in self.__canCtrlIdPool:
                ethData = self.__canLen+self.__canCtrlIdPool[i]+self.canCtrlDataPool[i]
                self.sendto(ethData, self.remote_addr)
                # print(ethData)
                time.sleep(1)      #发送一帧的间隔

    def canChangeSendData(self, canIdName, canData):
        '''
        修改can发送中的data值:
            需要一帧一帧修改
            与canSend()配合使用 建议使用线程锁以防止修改中同时发送数据造成数据错误
            canIdName:str类型 can的id 与init中定义的相同 4字节 ie:"Gear_Shift_Cmd"
            canData:byte类型 can的数据 8字节
        '''
        if type(canData) == type(bytes()) and len(canData) == 8:     #检验candata的类型和长度
            self.canCtrlDataPool[canIdName] = canData
            print(canIdName, canData)
        else:
            print(">>> canData input err!!!")








if __name__ == "__main__":
    def callback():
        print("i am in callback")
    
    server = iVistaCan(socket.AF_INET, socket.SOCK_DGRAM)

    # server.canChangeSendData("Gear_Shift_Cmd", b"\x00\x00\x00\x00\x00\x00\x00\x00")

    # server.canSend()

    # server.bind(server.local_addr)
    # while True:
    #     data,client_addr = server.recvfrom_exe(1024, callback)