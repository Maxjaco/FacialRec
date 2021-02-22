import socket
import subprocess

ADDR = ('0.0.0.0', 8000)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print('listening ...')

while True:
    conn, addr = serv.accept()
    myfile = open('rec_movie.h264', 'wb')

    while True:
        data = conn.recv(BUFSIZE)
        if not data: break
        myfile.write(data)
        print('writing file ....')

    myfile.close()
    print('finished writing file')
    conn.close()
    print('client disconnected')
    break

