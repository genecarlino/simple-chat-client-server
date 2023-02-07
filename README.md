README for speak and speakd programs

Introduction

The speak and speakd programs are two separate scripts written in Python that communicate with each other over a network using the socket interface to TCP on the local machine. They follow the old-fashioned chat protocol, where one side writes and the other listens. The two programs alternate between writing and listening, with the current writer continuing to write until control is relinquished. 

How to run the programs


Server
To run the speakd server program, use the following command in the terminal:

            python3 speakd.py

The program will automaticaly connect to the local host. It will ask the user to enter in a port number that the server should  should listen for incoming connections. If the socket is taken or invalid the user will be notified of an error and asked to reconnect until a valid port is chosen.

The picture below shows what the terminal should look like when you enter in a valid port and the server has connected. 


<img width = "153" alt = "Click for Photo" src = "https://imgur.com/a/j2fBtxC">


Client
To run the speak client program, use the following command in the terminal:

             python3 speak.py

The Program will connect to the local host but ask the user to choose a port that they would like to connect to. If the port is being used or if the port is invalid and error will occur and the user will be notified and asked to choose a new port number. 

The picture below shows what the terminal should look like when you enter in a valid port and the client has connected to the server.

<img width = "153" alt = "Click for Photo" src = "https://imgur.com/gallery/fsdRccF">

When a client has connected to the server, the server will print where the accepted connection is coming from. You might see that the accepted connection is different that the port you entered to start the program.Note that the speak.py program creates a new connection to send data from after it connects to the server port.

<img width = "153" alt = "Photo of terminal running speakd" src = "https://imgur.com/gallery/W8UnEdU">

Functionality

The speak client program connects to the speakd server program, which is waiting for a client. The client gets to write first, and the two programs alternate writing. A message is considered complete when either side inputs 'x' on a line by itself. If either side inputs 'xx' on a line by itself, the chat is to be ended and the connection is terminated.


Note

This code is meant to serve as a starting point, and can be further modified and improved to fit your needs.


