# Server code

import socket
import sys

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = "localhost"
while True:

    try:
        port = int(input("Enter the port of the server: "))
        server_socket.bind((host, port))
        break
    except:
        print("Error: Try another Port")



# Listen for incoming connections, allowing only one connection
server_socket.listen(1)
# print(f"Listening on {host}:{port}")
print(f"Listening on port # {port}")
# Accept incoming connection
connection, address = server_socket.accept()
print(f"Accepted connection from {address[0]}:{address[1]}")

# Set initial state to "listening"
state = "listening"

# Start the chat
while True:
    # If state is "listening", receive message from client
    if state == "listening":
        data = connection.recv(1024).decode('utf-8')
        if data == 'xx':
            break
        print(f"Client: {data}")
        ack_message = "Message Received, Total size:" + str(sys.getsizeof(data))
        connection.send(ack_message.encode('utf-8'))


        # If the message is 'x', change state to "sending"
        if data == 'x':
            state = "sending"
            continue

    # If state is "sending", send reply to client
    if state == "sending":
        message = input("Server: ")
        connection.send(message.encode('utf-8'))
        data = connection.recv(1024).decode('utf-8')
        print(f"Server: {data}")
        if message == 'xx':
            break

        # If the message is 'x', change state to "listening"
        if message == 'x':
            state = "listening"

# Close the connection and socket
connection.close()
server_socket.close()
