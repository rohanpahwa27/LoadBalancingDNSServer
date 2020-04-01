import threading
import time
import random
import socket as mysoc
import sys
from collections import defaultdict

TS2dict = defaultdict(list)
# Structure of TS2dict:

# TS2dict = {

# 'Hostname': ['link1','link2','link3']
# 'IP Address': ['ipaddr1', 'ipaddr2','ipaddr3']
# 'Flag': ['flag1','flag2','flag3']

# }

# Structure of TS2dict

# server task
def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print(err)
    server_binding=('',port)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)

    num = csockid.recv(1024).decode()
    print("DATA:", num)

    for j in range (int(num)):
        data = csockid.recv(1024).decode().strip().lower()
        if (data in TS2dict.get("Hostname")):
            index = TS2dict.get("Hostname").index(data)
            #print(data,TS2dict.get("IP Address")[index],TS2dict.get("Flag")[index])
            findata = data + " " + TS2dict.get("IP Address")[index] + " " + TS2dict.get("Flag")[index]
            #print(findata)
            csockid.send(findata.encode('utf-8'))
        # print(data.decode())

   # Close the server socket
    ss.close()
    exit()

data = []
f = open('PROJ2-DNSTS2.txt','r')
while True:
  line = f.readline()
  if not line:
    break
  currline = line.strip() #gets line as words per line
  data.append(currline.split()) #separates each word in line into entries in self-generated list


filelen = len(data)

for i in range(3): #traversing over HN, IPADDR, FL, populates RSDict
  for j in range(filelen):
    if i+1 == 1:
      TS2dict['Hostname'].append(data[j][i].lower())
    if i+1 == 2:
      TS2dict['IP Address'].append(data[j][i])
    if i+1 == 3:
      TS2dict['Flag'].append(data[j][i])

if (len(sys.argv) == 2):
    port = int(sys.argv[1])
    to_client = threading.Thread(name='server', target=server)
    to_client.start()