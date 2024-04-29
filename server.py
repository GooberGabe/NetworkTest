import socketserver

# Define a custom handler to manage client connections
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("New client connected:", self.client_address)
        self.request.sendall(b"Welcome to the server!\n")

        # Listen for messages from the client and broadcast them to all connected clients
        while True:
            data = self.request.recv(1024).strip()
            if not data:
                break
            print(f"Received from {self.client_address}: {data.decode()}")
            self.broadcast(data)

    def broadcast(self, data):
        for client in clients:
            client.sendall(data)

# Create a list to store connected clients
clients = []

# Define the server settings
HOST, PORT = "localhost", 9999

# Create the server object
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

# Start the server to listen for incoming connections
server.serve_forever()
