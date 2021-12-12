import pickle
import socket
import sys
import oneNN as on
import numpy as np
import time
import socketserver
from mongoConn import Connection_DB
from film_sugg import Film_Suggestor

def get_from_string_to_original(string_array):
    array = []
    for string in string_array:
        array.append(float(string))  
    return np.asarray(array)

def get_users_from_string(string_array):
    array = []
    for string in string_array:
        array.append(string)  
    return array

def get_string_from_array(suggestions):
    return "/".join(x for x in suggestions)

def get_entire_message(connection):
    message = ""
    counter = 0
    while True:
        
        message_piece = connection.recv(2000)
        if not message_piece:
            break
        else:
            message_part = message_piece.decode()
            message_part_splitted = message_part.split('_fine_messaggio')
            if(len(message_part_splitted)>1):
                message += message_part_splitted[0]
                #print(message_part_splitted[1])
                break
            else:
                message += message_part_splitted[0]
    #connection.close()
    return message.split('new_part_')



class MyTCPHandler(socketserver.BaseRequestHandler):

  def handle(self):

    # Receiving command from the client
    received_message = get_entire_message(self.request)
    #print(received_message[1])
    if(received_message[1]=='login'):
        #print('sono qui')
        print(received_message[1])
        string_array = received_message[2]
        #print("string features",string_array)
        print("original features",get_from_string_to_original(string_array.split('/')))
        if(np.random.randint(0,2)==0):
            self.request.sendall(('new_part_successo_fine_messaggio').encode())
        else:
            self.request.sendall(('new_part_fallimento_fine_messaggio').encode())
            
    elif(received_message[1]=='registration'):
        print(received_message[1])
        username = received_message[2]
        print(username)
        string_array = received_message[3]
        #print("string features",string_array)
        print("original features",get_from_string_to_original(string_array.split('/')))
        if(np.random.randint(0,2)==0):
            self.request.sendall(('new_part_successo_fine_messaggio').encode())
        else:
            self.request.sendall(('new_part_fallimento_fine_messaggio').encode())        
    else:
        print(received_message[1])
        users = get_users_from_string(received_message[2])
        cd = Connection_DB()
        interest = [cd.get_random_best_common_interests(users,'film_interest')]
        cd.close()
        fs = Film_Suggestor()
        films = fs.provide_suggestions(interest)
        string_suggestions = get_string_from_array(films)
        self.request.sendall(('new_part_'+string_suggestions+'_fine_messaggio').encode())
        
    print("Request ended !!")

def server_program():
    HOST = socket.gethostbyname(socket.gethostname())
    print("host",HOST)
    PORT = 5000
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
   
if __name__ == '__main__':
    server_program()