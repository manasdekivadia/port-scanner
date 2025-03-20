# Importing Libraries
import sys
import socket 
import time
import threading
import pyfiglet

# Intro
usage = "Syntax : python3 port_scanner.py IP start_port end_port"
print("-" * 70)
font = pyfiglet.Figlet()
ascii_art = font.renderText("PORT SCANNER")
print(ascii_art)
print(" "*50 + "By Manas Dekivadia")
print("-" * 70)

# Argument Conditioning
start_time = time.time()
if(len(sys.argv) != 4):
    print(usage)
    sys.exit()
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution Error")
    sys.exit()


# Argument Capturing
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])


# Scanning Function
print("Scanning Target : ", target)
def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target,port))
    if(conn):
        print(f"Port {port} is OPEN ")
    else:
        try:
            print(f"Port No: {port} Open Protocol Service Name : {socket.getservbyport(port,'tcp')}")
        except socket.error:
            print(f"Port No : {port} Open Protocol Service Name : Unknown")
    s.close()


for port in range(start_port,end_port+1):
    thread = threading.Thread(target=scan_port,args=(port,))
    thread.start()


# Elapsed Time
end_time = time.time()
print("Time Elapsed : ",end_time - start_time,"s")