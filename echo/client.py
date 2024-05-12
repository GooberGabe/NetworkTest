import socket
import os 
import threading

#server_ip = "10.255.14.116"
server_ip = "localhost"
server_port = 7000
server_address = (server_ip, server_port)

def connect():
    def reader(socket):
        while True:
            try:
                response = sock.recv(1024)
                response = str(response, "UTF-8")
                print()
                print(response)
                print()
            except:
                print("Client Disconnected")
                os._exit(0)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)
        print(f"Connected to: {server_address}")

        thread = threading.Thread(target=reader, args=(sock,))
        thread.start()

        name = input("What is your name? ")
        b_name = bytes(f"USER|{name}", "UTF-8")
        sock.sendall(b_name)

        print("Enter your messages to send (exit to quit): ")
        while True:
            message = input()
            if message == "exit":
                break
            if message == "users":
                message = bytes(f"DIR", "UTF-8")
            elif "whisper" in message:
                text = " ".join(message.split(" ")[1:])
                message = bytes(f"WHS|{name}>{text}", "UTF-8")
            else:
                message = bytes(f"MSG|{message}", "UTF-8")
            sock.sendall(message)

    print("Client closed.")

if __name__ == '__main__':
    connect()