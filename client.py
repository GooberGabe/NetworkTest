import socket
import os 
import threading
from random import *

#server_ip = "10.255.14.116"
server_ip = "localhost"
server_port = 7000
server_address = (server_ip, server_port)

class Connection (object):
    def __init__(self, socket, name):
        self.socket = socket
        self.name = name

CONNECTION = Connection(None, "Default")

# Called from app.py
def process_message(message):
    message = bytes(f"{CONNECTION.name}|{message}", "UTF-8")
    CONNECTION.socket.sendall(message)

# Wrapper for _connect
def connect():
    thread = threading.Thread(target=_connect)
    thread.start()

# Establish and maintain connection
def _connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        CONNECTION.socket = sock
        print(f"Connected to: {server_address}")

        while True:
            try:
                # Receive response from the server and send it to the frontend
                response = sock.recv(1024)
                response = str(response, "UTF-8")
                print()
                print(response)
                

            except:
                print("Client Disconnected")
                #os._exit(0)
                break

    print("Client closed.")

if __name__ == '__main__':
    connect()