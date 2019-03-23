## server.py

import socket
import argparse
import os

def run_server(port=4000):
    host = ''

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1) ## max client 1
        conn, addr = s.accept()
        fileName = conn.recv(1024)
        fileLink = args.d + "/" + fileName.decode()
        print("Search_file_name :", fileName.decode())
        if os.path.exists(fileLink):
                with open(fileLink, 'rb') as f:
                        data = f.read(1024) # 1024바이트씩 파일을 읽음
                        while data: # data가 null값일때까지 반복
                                conn.send(data)
                                data = f.read(1024)
                fileSize = os.path.getsize(fileLink)
                print("File transfer success.")
                print("File_size :", fileSize, "byte")
        else:
                print("File search failed.")
                print("File does not exist.")
        conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port -d directory")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-d', help="directory", required=True)

    args = parser.parse_args()
    run_server(port=int(args.p))