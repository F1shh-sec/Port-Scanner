# client - port scanner
# Goal - Find open ports

import socket
import sys
#usage: Python port_scanner.py www.nmap.org 1 200
try:
    host = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
except IndexError as e:
    print("Usage: Python port_scanner.py TargetIP Min_Port Max_port")
    print(e)
    min_port = 1
    max_port = 200
print("# of filtered ports will be printed at the end")
# Filtered ports are spammy so i just printed the number of filtered ports at the end

filtered = 0
for port in range(min_port, max_port+1):
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.settimeout(0.1)
        client_sock.connect((host, port))
        # Open port - do nothing
        # Closed port - OS error
        # Filtered port - Block
        print(f"port {port} is open")
    except socket.timeout:
        filtered += 1
    except OSError:
        print(f"port {port} is closed")

    client_sock.close()
print(f"There are {filtered} filtered ports")