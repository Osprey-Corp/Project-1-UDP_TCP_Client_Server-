import socket

# CONSTANTS
HOST     = '127.0.0.1' # Loopback Interface IP
TCP_PORT = 65432       # Designated TCP Port
UDP_PORT = 5005        # Designated UDP Port 

# Data that will be sent and capitalized
data_list = ["abcdef abc123def", "ABcdEF", "AB12cdEF", "Two Words HERE !!"] 

# Menu for the user to choose between sending data in TCP or UDP
option = input("Choose Client Protocol:\n1.TCP\n2.UDP\nInput: ")

######################
# TCP CLIENT
######################
if option == "1":
    
    # Create socket object. SOCK_STREAM parameter makes it a TCP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        # Connect to socket in server
        sock.connect((HOST, TCP_PORT))

        # Iterate over data list
        for data in data_list:

            # Send data to server encoded in byte format
            print('Sending:  ' + data)
            sock.sendall(data.encode())
            
            # Decode data into string and display data received from server 
            data = sock.recv(1024).decode()
            print('Received: ' + data + '\n')

######################
# UDP CLIENT
######################
elif option == "2":

    # Create socket object. SOCK_DGRAM parameter makes it a UDP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

        # Iterate over data list
        for data in data_list:

            # Send data to server encoded in byte format
            print('Sending:  ' + data)
            sock.sendto(data.encode(), (HOST, UDP_PORT))

            # Decode data into string and display data received from server 
            data = sock.recv(1024).decode()
            print('Received: ' + data + '\n')
