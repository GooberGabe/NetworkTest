import socket
import requests

# Server address
SERVER_HOST = "localhost"
SERVER_PORT = 9999

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to the server.")

    # Receive welcome message
    print("Server says:", sock.recv(1024).decode())

    # Access GitHub Pages site
    github_page = requests.get("https://goobergabe.github.io/NetworkTest")
    print("GitHub Pages content:", github_page.text)

    # Example: Sending a message to the server
    message = input("Enter your message: ")
    sock.sendall(message.encode())
