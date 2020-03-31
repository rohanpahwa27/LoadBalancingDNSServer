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
    server_binding=('',lsport)
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
    ts1.connect((mysoc.gethostbyname(ts1host),ts1port))
    ts1.settimeout(1)
    ts2.connect((mysoc.gethostbyname(ts2host),ts2port))
    ts2.settimeout(1)

    num = csockid.recv(1024)
    ts1.send(num)
    ts2.send(num)
    
    # get data from client.py and send to both top level servers 
    for j in range (int(num)):
        data = csockid.recv(1024)
        senddata = data.decode()
        ts1.send(senddata.encode('utf-8'))
        ts2.send(senddata.encode('utf-8'))
        time.sleep(0.1)
        findata1 = ""
        findata2 = ""
        try:
            ts1data = ts1.recv(1024).decode()
            findata1 = ts1data
            #print(findata1, "hello")
        except:
            ts1data = ""
        
        try:
            ts2data = ts2.recv(1024).decode()
            findata2 = ts2data
            #print(findata2, "hello")
        except:
            ts2data = ""
        
        if (ts1data == "" and ts2data == ""):
            #print(senddata," - ERROR:HOST NOT FOUND")
            data_to_client = str(senddata) + " " + "-" + " " + "ERROR:HOST NOT FOUND"
            csockid.send((data_to_client).encode('utf-8'))
        else:
            if(findata2 == "" and findata1 != ""):
                #print(findata1,"hi :)")
                data_to_client = findata1
                csockid.send(data_to_client.encode('utf-8'))
            else:
                #print(findata2,"hi :)")
                data_to_client = findata2
                csockid.send((data_to_client).encode('utf-8'))

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

if (len(sys.argv == 6)):
    lsport = int(sys.argv[1])
    ts1host = sys.argv[2]
    ts1port = int(sys.argv[3])
    ts2host = sys.argv[4]
    ts2port = int(sys.argv[5])
    to_client = threading.Thread(name='server', target=server)
    to_client.start()

# ts1thread = threading.Thread(name = 'client', target = client(ts1port))
# ts2thread = threading.Thread(name = 'client', target = client(ts2port))