## client

import time
import socket
import threading
import argparse

flag = True

def send():
    while True:
        msg = input()
        s.sendall(msg.encode())

def read():
    global flag
    while True:
        msg = s.recv(1024)
        if msg.decode() == "채팅이 정상 종료되었습니다.":
            print('From ', args.i, ':', args.p, msg.decode())
            flag = False
            break
        else:
            print('From ', args.i, ':', args.p, msg.decode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)

    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.i, int(args.p)))
        sendT = threading.Thread(target=send, args=(), daemon = True)
        readT = threading.Thread(target=read, args=())
        sendT.start()
        readT.start()
        print("** 채팅 종료 명령어 (:quit) **")
        while flag:
            time.sleep(1)