import socket
import threading

#server_ip = "10.255.14.116"
server_ip = "localhost"
server_port = 7000
server_address = (server_ip, server_port)

clients = {} # Key = Connection, Value = Username
clients_lock = threading.Lock()

def broadcast(message, connection):
    with clients_lock:
        user = clients[connection]
        message = bytes(f"{user}: {message}", "UTF-8")
        for client in clients.keys():
            if client != connection:
                client.sendall(message)

def client_connect(connection, address):
    with clients_lock:
        clients[connection] = address
    while True:
        try:
            data = connection.recv(1024)
            data = str(data, "UTF-8")
            
            if (len(data) > 0):
                print(f"Received: {data}")
                response = bytes(data, "UTF-8")
                
                broadcast(data, connection)
        except Exception as e:
            print(f"[ERR] {e}")
            break 

    print(f"Client Disconnected: {address}.")
    with clients_lock:
        del clients[connection]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(server_address)
    sock.listen()
    print(f"Server started: {server_address}")

    while True:
        connection, address = sock.accept()
        print(f"Client Connected: {connection} {address}")
        client_thread = threading.Thread(target=client_connect, 
                                         args=(connection,address))
        client_thread.start()

