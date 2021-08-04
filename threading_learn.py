#!/usr/bin/python3

import threading

exitFlag = 0

class recTopic (threading.Thread):            #接收topic的线程
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        pass

class sendToETH (threading.Thread):           #发送至以太网的线程
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("开始线程：" + self.name)
        print ("退出线程：" + self.name)


if __name__ == "__main__":
    # 创建新线程
    thread1 = recTopic(1, "recTopic")
    thread2 = sendToETH(2, "sendToETH")

    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print ("退出主线程")