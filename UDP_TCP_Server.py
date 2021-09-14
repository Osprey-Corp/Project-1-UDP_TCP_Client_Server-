import socket

# CONSTANTS
HOST     = '127.0.0.1'
TCP_PORT = 65432
UDP_PORT = 5005

# User menu to choose whether to listen for a TCP or DCP connection
option = input("Choose Server Listener:\n1.TCP\n2.UDP\nInput: ")

######################
# TCP SERVER LISTENER
######################
if option == "1":
    
    print("Listening for TCP in PORT 65432...")

    # Create socket object. SOCK_STREAM parameter makes it a TCP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        # Bind to designated TCP Port and start listening
        sock.bind((HOST, TCP_PORT))
        sock.listen()

        # Wait for incoming client connection
        conn, addr = sock.accept()

        # Once connected iterate over data being recived from TCP Client
        with conn:
            while True:
                # Decode data being received and capitalize
                data = conn.recv(1024).decode().upper()
                
                # End connection once data stops being received
                if not data:
                    break

                # Return to client data they sent but capitalized
                conn.sendall(data.encode())

######################
# UDP SERVER LISTENER
######################
elif option == "2":

    print("Listening for UDP in PORT 5005...")
    
    # Create socket object. SOCK_STREAM parameter makes it a TCP Socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:


        sock.bind((HOST, UDP_PORT))

        while True:
            # Receive data from client
            data, address = sock.recvfrom(1024)

            # Decode data being received and capitalize
            data = data.decode().upper()

            # Return to client data they sent but capitalized
            sock.sendto(data.encode(), address)
