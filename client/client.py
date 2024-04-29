import socket

# Server address
HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    # Send data to server
    sock.sendall(b"Hello, server")
    # Receive data from server and print it
    received = sock.recv(1024)
    print("Received:", received.decode())
