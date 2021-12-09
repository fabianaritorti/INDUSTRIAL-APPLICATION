import socket
import pickle
import features_extract as fe
import easter_egg as ee
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
from playsound import playsound
import time
import numpy
import numpy
'''
def send_message(host,port,message):
    tcp_socket = socket.create_connection(('192.168.1.107', 5000))
    tcp_socket.sendall(message)
    tcp_socket.close()
'''

'''
def check_same_array(arr1,arr2,n1,n2):
    if n1!=n2:
        print("dim diverse")
        return False
    print("arr1",arr1)
    print("arr2",arr2)
    for i in range(n1):
        if(arr1[i]!=float(arr2[i])):
            return False
    #if none of the above conditions satisfied return true
    return True
'''

def check_same_array(arr1,arr2,n1,n2):
    if n1!=n2:
        print("dim diverse")
        return False
    #print("arr1",arr1)
    #print("arr2",arr2)
    for i in range(n1):
        if(arr1[i]!=arr2[i]):
            return False
    #if none of the above conditions satisfied return true
    return True

def get_string_from_array(average_desc):
    return "/".join(str(x) for x in average_desc)

def get_from_string_to_original(string_array):
    array = []
    for string in string_array:
        array.append(float(string))
    return numpy.asarray(array)
    

def client_program():

    try:
        #start_string = 'new_part_'
        data = 'new_part_login'
        frame,detected_face,average_desc = fe.get_average_features('login')
        string_array = get_string_from_array(average_desc[0])
        print(type(average_desc[0]))
        print("user_features",average_desc[0])
        #print("string_array",string_array)
        original_array = get_from_string_to_original(string_array.split('/'))
        print(type(original_array))
        print("reconstructed_array",original_array)
        if(check_same_array(average_desc[0],original_array,len(average_desc[0]),len(original_array))):
            print("sono gli stessi")
        else:
            print("sono diversi")
        tcp_socket = socket.create_connection(('192.168.1.107', 5000))
        data += 'new_part_'
        data += string_array
        tcp_socket.sendall(data.encode())
        '''
        tcp_socket = socket.create_connection(('192.168.1.107', 5000))
        data += 'new_part_'
        data += string_array
        tcp_socket.sendall(data.encode())
        '''
        '''
        if(check_same_array(average_desc[0],original_array,len(average_desc[0]),len(original_array))):
            print("sono gli stessi")
        else:
            print("sono diversi")
        '''
        
        '''
        tcp_socket = socket.create_connection(('192.168.1.107', 5000))
        #tcp_socket.sendall(data.encode())
        msg.extend(data.encode())
        print("average desc",average_desc[0])
        data = pickle.dumps(average_desc[0])
        dim = len(data)
        msg.extend(str(dim).encode())
        #msg.extend(data)
        #tcp_socket.sendall(str(dim).encode())
        tcp_socket.sendall(msg)
        '''
    
    finally:
        print("Closing socket")
        tcp_socket.close()
    

if __name__ == '__main__':
    client_program()