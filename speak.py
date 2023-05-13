# Client code

import socket
import sys

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the host and port
host = "localhost"
while True:
    try:
        port = int(input("Enter the port of the server: "))
        # Connect to the server
        client_socket.connect((host, port))
        break
    except:
        print("Error")
        client_socket.close()
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set initial state to "sending"
state = "sending"

# Start the chat
while True:
    # If state is "sending", send message to server
    if state == "sending":
        message = input("Client: ")
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {data}")

        if message == 'xx':
            break

        # If the message is 'x', change state to "listening"
        if message == 'x':
            state = "listening"

    # If state is "listening", receive reply from server
    if state == "listening":
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {data}")
        ack_message = "Message Received, Total size:" + str(sys.getsizeof(data))
        client_socket.send(ack_message.encode('utf-8'))

        if data == 'xx':
            break

        # If the message is 'x', change state to "sending"
        if data == 'x':
            state = "sending"

# Close the client socket  
client_socket.close()

#end of code
