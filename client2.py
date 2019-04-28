# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:01:01 2019

@author: melkhafef
"""
def client_receive(s) :
    while True :
        x=s.recv(2048)
        print("server:",x.decode('utf-8'))
try:
    from socket import *
    from threading import Thread
    s=socket(AF_INET,SOCK_STREAM)
    host="127.0.0.1"
    port=8001
    s.connect((host,port))
    Thread(target=client_receive,args=(s,)).start()
    while True :
        s.send((input("I:")).encode('utf-8'))
    s.close()
except error as e :
    print(e)
except KeyboardInterrupt :
    print('Ok')
    