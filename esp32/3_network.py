import network
import time
from socket import *

wlan = network.WLAN(network.STA_IF)
wlan.active(True)



def do_connect():
    if not wlan.isconnected():
        print("unconnect")
        for i in wlan.scan():
            print(i)
            if i[0] == b'H3C_1102':
                wlan.connect('H3C_1102', '18950077001')
                break
            if i[0] == b'qkids_guest':
                wlan.connect('qkids_guest', 'qkidsguest')
                break
        while not wlan.isconnected():
            time.sleep(0.1)
            print("connecting...")
    print(wlan.ifconfig())

def run():
    

    # 1. 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 2. 准备接收方的地址
    dest_addr = ('192.168.124.3', 9876)

    # 3. 从键盘获取数据
    send_data = "ok red "

    # 4. 发送数据到指定的电脑上
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    do_connect()
    run()
