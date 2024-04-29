from flask import Flask, render_template, request
import socket

app = Flask(__name__)

# Server address
HOST, PORT = "localhost", 9999

@app.route('/')
def index():
    return render_template('server.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        # Send data to server
        sock.sendall(message.encode())
        # Receive data from server and return it
        received = sock.recv(1024)
        return received.decode()

if __name__ == '__main__':
    app.run(debug=True)
