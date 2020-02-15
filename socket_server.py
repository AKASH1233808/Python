#Server side

import socket

def server_program():
    # get the hostname
    host = socket.gethostname()

    # initiate port no above 1024
    port = 5000  

    server_socket = socket.socket()
    
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
