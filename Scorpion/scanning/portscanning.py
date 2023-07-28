import socket
import sys
import time

top_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 587, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443, 8888, 9000, 9001, 9090, 9100, 9200, 9300, 10000, 10050, 10051, 11211, 27017, 27018, 27019, 28017, 50000, 50070, 50030, 50060, 50075, 50090, 5432, 5984, 6379, 7001, 7002, 8000, 8001, 8002, 8008, 8081, 8082, 8088, 8090, 8091, 8444, 8880, 8883, 8888, 9001, 9090, 9091, 9200, 9300, 9418, 9999, 11211, 27017, 27018, 27019, 28017, 50000, 50070, 50030, 50060, 50075, 50090, 5432, 5984, 6379, 7001, 7002, 8000, 8001, 8002, 8008, 8081, 8082, 8088, 8090, 8091, 8444, 8880, 8883, 8888, 9001, 9090, 9091, 9200, 9300, 9418, 9999]


def scanPort(host, port):
    """
    Scan a given host and port to check if the port is open or closed.

    Parameters:
        host (str): The IP address or hostname of the target host.
        port (int): The port number to scan.

    Returns:
        str: A message indicating whether the port is open or closed.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        return "Port " + str(port) + " is open\n"
    except:
        return "Port " + str(port) + " is closed\n"

def scanTopPorts(host, display=False):
    if display == False:
        openPorts = []
        for port in top_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, port))
                sock.close()
                openPorts.append(port)
            except:
                pass
        return openPorts
    else:
        for port in top_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, port))
                sock.close()
                print("Port " + str(port) + " is open")
            except:
                print("Port " + str(port) + " is closed")