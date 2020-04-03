# LoadBalancingDNSServer
Abhishek Modoor (avm67) & Rohan Pahwa (rp930)

LS Functionality: 
The LS functionality of tracking which TS responded to the query and appropriately timing out if neither TS responded is done by setting an initial sleep that is greater than 2 * timeout for one socket. This is so that if both timeout, there is enough time in between prior to sending the next string. 

Issues:
There aren't any known issues that is currently not working in our code

Problems during development:
Ensuring that we were able to connect both TS servers and ensuring proper timeout if neither server responded. Formatting of the string to ensure proper response (sending {Hostname + IP Address + Flag} or {Hostname - ERROR: HOST NOT FOUND}) back to LS and sending it to the RESOLVED.txt in client. 

What did you learn: 
How to implement load balancing among servers such that only the TS that contains the hostname query may respond back to the LS. How to ensure proper timeout in the case that neither TS responds and how to work together in a collaborative setting to construct the project. 
