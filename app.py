from flask import Flask, render_template, request
from client import connect

app = Flask(__name__)

@app.route('/')
def index():
    connect()
    return render_template('index.html')

@app.route('/post-message', methods=['POST'])
def post_message():
    message_content = request.form.get('message')
    #message_content = "yarg!"
    # Call your client.py script here and pass the message content
    from client import process_message
    process_message(message_content)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)