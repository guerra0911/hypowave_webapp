from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
socketio = SocketIO(app)

# Global variable to store the latest packet
latest_packet = None

@app.route('/')
def index():
    # Render the index template with the latest packet
    return render_template('index.html', packet=latest_packet)

@socketio.on('connect')
def handle_connect():
    print('Client connected:', request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected:', request.sid)

@socketio.on('event_name')
def handle_my_custom_event(json_data):
    global latest_packet
    print('received json:', json_data)
    latest_packet = json_data  # Update the latest packet
    emit('response_event', {'data': 'Response from server'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
