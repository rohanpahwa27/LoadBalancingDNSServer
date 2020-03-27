import threading
import time
import random
import socket as mysoc
import sys
from collections import defaultdict

TS1dict = defaultdict(list)
# Structure of TS1dict:

# TS1dict = {

# 'Hostname': ['link1','link2','link3']
# 'IP Address': ['ipaddr1', 'ipaddr2','ipaddr3']
# 'Flag': ['flag1','flag2','flag3']

# }

# Structure of TS1dict

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
        if (data in TS1dict.get("Hostname")):
            index = TS1dict.get("Hostname").index(data)
            print(data," ",TS1dict.get("IP Address")[index]," ",TS1dict.get("Flag")[index])
            csockid.send((data+" "+TS1dict.get("IP Address")[index]+" "+TS1dict.get("Flag")[index]).encode())
        # print(data.decode())
        

   # Close the server socket
    ss.close()
    exit()

data = []
f = open('PROJ2-DNSTS1.txt','r')
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
      TS1dict['Hostname'].append(data[j][i].lower())
    if i+1 == 2:
      TS1dict['IP Address'].append(data[j][i])
    if i+1 == 3:
      TS1dict['Flag'].append(data[j][i])



# how to read a text file in python
# with open("PROJI-DNSRS.txt") as f:
#   while True:
#     c = f.read(1)
#     print("".join(["EOF: ", c]))
#     if not c:
#       print ("End of file")
#       break
#     print ("".join(["Read a character:",c," ","hi"]))

if (len(sys.argv) == 2):
    port = int(sys.argv[1])
    to_ls = threading.Thread(name='server', target=server)
    to_ls.start()