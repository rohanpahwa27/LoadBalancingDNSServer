#client task
import sys
import threading
import time
import random
import socket as mysoc
from collections import defaultdict

CLdict = defaultdict(list)
# Structure of CLdict:

# CLdict = {
# 'Hostname': ['link1','link2','link3']
# }

# Structure of CLdict

def client():
    #connect to ls socket
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print(err)

 # Define the port on which you want to connect to the server
    # port = rsport
    port = 52799
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
 # connect to the server on local machine
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

    

    #sends length of strings to send to root server to check if its there
    cs.send(str(len(CLdict.get('Hostname'))).encode())
    time.sleep(0.1)
    
    #sends actual strings to root server (line by line)
    f = open("RESOLVED.txt", "a")
    for j in range(len(CLdict.get('Hostname'))):
        datasent = CLdict.get('Hostname')[j]
        cs.send(datasent.encode('utf-8'))
        time.sleep(4.1)
        data = cs.recv(1024).decode() 
        f.write(data+"\n")   
    cs.close()
    exit()


data = []
f = open('PROJ2-HNS.txt','r')
while True:
  line = f.readline()
  if not line:
    break
  currline = line.strip() #gets line as words per line
  data.append(currline.split()) #separates each word in line into entries in self-generated list


filelen = len(data)

 #traversing over HN
for j in range(filelen):
  CLdict['Hostname'].append(data[j][0].lower())

for j in range(len(CLdict.get('Hostname'))):
    print(CLdict.get('Hostname')[j])


# print(CLdict)



# if (len(sys.argv) == 3):
#     lshost = sys.argv[1]
#     tshost = sys.argv[2]
#     rsthread = threading.Thread(name='client', target=client)
#     rsthread.start()

lsthread = threading.Thread(name='client', target=client)
lsthread.start()
        # input("Hit ENTER  to exit")
# exit()