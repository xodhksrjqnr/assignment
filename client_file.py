## client.py

import socket
import argparse
import os

def run(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(args.f.encode())
        data = s.recv(1024)
        if not data:
                print("File does not exist.")
        else:
                with open('./' + args.f, 'wb') as f:
                        while data:
                                f.write(data)
                                data = s.recv(1024)
                fileSize = os.path.getsize(args.f)
                print("File transfer success.")
                print("File name : ", args.f , " File size : ", fileSize, " byte")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host -f filename")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)
    parser.add_argument('-f', help="file_name", required=True)

    args = parser.parse_args()
    run(host=args.i, port=int(args.p))