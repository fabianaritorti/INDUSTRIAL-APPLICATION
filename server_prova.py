import pickle
import socket
import sys
import oneNN as on
import numpy as np
import time


def get_from_string_to_original(string_array):
    array = []
    for string in string_array:
        array.append(float(string))  
    return np.asarray(array)

def get_entire_message(connection):
    #connection, client = server.accept()
    message = ""
    counter = 0
    while True:
        
        message_piece = connection.recv(100000000)
        if not message_piece:
            break
        else:
            message += message_piece.decode()
            print(counter)
            counter+=1
    #connection.close()
    return message.split('new_part_')

'''    
def get_features(server,dim):
    connection, client = server.accept()
    features = connection.recv(dim)
    connection.close()
    return features
'''


def server_program():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    print("host",host)
    server_address = (host, port)
    
    server.bind((host,port))
    
    server.listen(5)
    print("inizio a sentire")
    
    #conn, address = server.accept()  # accept new connection
    
    while True:
        try:
            connection, client = server.accept()
            received_message = get_entire_message(connection)
            #print(received_message[1])
            if(received_message[1]=='login'):
                string_array = received_message[2]
                #print("string features",string_array)
                print("original features",get_from_string_to_original(string_array.split('/')))
            connection.close()
            #received_dim = int(get_entire_message(server))
            #print(str(received_dim))
            #features = pickle.loads(get_features(server,received_dim))
            #print(features)
        finally:
            break
    server.close()
    
    #conn.close()  # close the connection

if __name__ == '__main__':
    server_program()