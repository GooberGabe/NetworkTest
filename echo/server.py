import socket
import threading

#server_ip = "10.255.14.116"
server_ip = "localhost"
server_port = 7000
server_address = (server_ip, server_port)

clients = {}
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
            
            print(f"Received: {data}")
            request = data.split("|")
            if len(request) == 0:
                response = bytes("NOK", "UTF-8")
                connection.sendall(response)
            elif request[0] == "USER" and len(request) == 2:
                user = request[1]
                with clients_lock:
                    clients[connection] = user
                response = bytes("USER_OK", "UTF-8")
                connection.sendall(response)
            elif request[0] == "MSG" and len(request) == 2:
                broadcast(request[1], connection)
                response = bytes("MSG_OK", "UTF-8")
                connection.sendall(response)
            elif request[0] == "WHS" and len(request) == 2:
                names = request[1].split(" ")[0]
                message = request[1].split(" ")[1]
                sender_name = names.split(">")[0]
                recipient_name = names.split(">")[1]
                # the first word after whisper should be the recipient's name
                recipient_connection = list(clients.keys())[list(clients.values()).index(recipient_name)]
                print(recipient_connection)
                response = bytes(f"[{sender_name} whispers]: {message}", "UTF-8")
                recipient_connection.sendall(response)

            elif request[0] == "DIR":
                with clients_lock:
                    users = ', '.join(clients.values())
                response = bytes(f"Users logged in: {users}", "UTF-8")
                connection.sendall(response)
            else:
                response = bytes("NOK", "UTF-8")
                connection.sendall(response)
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
        print(f"Client connected: {connection} {address}")
        client_thread = threading.Thread(target=client_connect, 
                                         args=(connection,address))
        client_thread.start()

