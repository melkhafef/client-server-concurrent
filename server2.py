# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:00:29 2019

@author: melkhafef
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:48:33 2019

@author: melkhafef
"""

from socket import *
from threading import Thread
def server(session,ip,port):
    Thread(target=server_receive,args=(session,)).start()
    while True : 
        session.send((input("server:")).encode('utf-8'))
def server_receive(session):
    while True :
        client_message=session.recv(2048)
        print("client.{}.{}:".format(ip,port),client_message.decode('utf-8'))
try:
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    host="127.0.0.1"
    port=8001
    s.bind((host,port))
    s.listen(10)
    sessions=[]
    while True :
         session,addr=s.accept()
         sessions.append(session)
         ip=addr[0]
         port=addr[1]
         print("{}.{} join to chat".format(addr[0],addr[1]))
         Thread(target=server,args=(session,ip,port)).start()
    s.close()
except error as e :
    print(e)
except KeyboardInterrupt :
    print("Ok")

