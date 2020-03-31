import threading
import time
import random
import socket as mysoc
import sys

def client(port):
    #connect to ls socket
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(err)

# Define the port on which you want to connect to the server
    # port = rsport

    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

    cs.settimeout(2)

    cs.close()
    exit()


# server task
def server():
    # create server to talk to client.py
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print(err)
    server_binding=('',52799)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)

    # create two connections to 2 servers
    try:
        ts1=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(err)
    
    try:
        ts2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(err)
# Define the port on which you want to connect to the server
    # port = rsport

# connect to the server on local machine
    ts1.connect((mysoc.gethostbyname(mysoc.gethostname()),50008))
    ts1.settimeout(1)
    ts2.connect((mysoc.gethostbyname(mysoc.gethostname()),50007))
    ts2.settimeout(1)

    num = csockid.recv(1024)
    ts1.send(num)
    ts2.send(num)
    
    # get data from client.py and send to both top level servers 
    for j in range (int(num)):
        data = csockid.recv(1024)
        ts1.send(data)
        ts2.send(data)
        time.sleep(0.1)
        try:
            ts1data = ts1.recv(1024).decode()
        except:
            ts1data = ""
        
        try:
            ts2data = ts2.recv(1024).decode()
        except:
            ts2data = ""
        
        if (ts1data == "" and ts2data == ""):
            print(data.decode(),"-ERROR NOT FOUND")
        else:
            print(data.decode(),"hi :)")

   # Close the server socket
    ts1.close()
    ts2.close()
    ss.close()
    exit()

# if (len(sys.argv == 6)):
#     lsport = sys.argv[1]
#     ts1host = sys.argv[2]
#     ts1port = sys.argv[3]
#     ts2host = sys.argv[4]
#     ts2port = sys.argv[5]
#     to_client = threading.Thread(name='server', target=server)
#     to_client.start()

to_client = threading.Thread(name='server', target=server)
to_client.start()

# ts1thread = threading.Thread(name = 'client', target = client(ts1port))
# ts2thread = threading.Thread(name = 'client', target = client(ts2port))