## server

import time
import socket
import threading
import argparse

flag = True
def send(conn):
    while True:
        msg = input()
        conn.sendall(msg.encode())

def read(conn, addr):
    global flag
    while True:
        msg = conn.recv(1024)
        if msg.decode() == ":quit":
            print("채팅 종료")
            flag = False
            break
        else:
            print('From ', addr[0], ':', addr[1], msg.decode())

if __name__ == '__main__':
    endMessage = "채팅이 정상 종료되었습니다."
    parser = argparse.ArgumentParser(description="Echo server -p port")
    parser.add_argument('-p', help="port_number", required=True)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(1)
    connect, address = server.accept()

    sendT = threading.Thread(target=send, args=(connect,), daemon = True)
    readT = threading.Thread(target=read, args=(connect, address))

    sendT.start()
    readT.start()

    while flag:
        time.sleep(1)
    connect.sendall(endMessage.encode())
    connect.close()

    server.close()