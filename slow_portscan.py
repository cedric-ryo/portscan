import socket

ip = "127.0.0.1"
s = socket.socket(2,1) #socket.AF_INET(IPv4), socket.SOCK_STREAM(TCP)

def porttry(ip, port):
    try:
        #connect to target
        s.connect((ip, port))
        return True
    except:
        return None
    
for port in range(0,100):
    value = porttry(ip, port)
    if value == None:
        print("Port not opend on %d" % port)
    else:
        print("Port opened on %d" % port)
    