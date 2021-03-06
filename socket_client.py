#Client side 

import socket

def client_program():
    
     # as both code is running on same pc
    host = socket.gethostname()            
    port = 5000   # socket server port number

    # instantiate
    client_socket = socket.socket()        
    client_socket.connect((host, port))
    
    # take input
    message = input(" -> ")      

    while message.lower().strip() != 'bye':

        # send message and receive response 
        client_socket.send(message.encode())         
        data = client_socket.recv(1024).decode()   

        print('Received from server: ' + data)   

         # again take input
        message = input(" -> ") 

     # close the connection
    client_socket.close()    


if __name__ == '__main__':
    client_program()
