import socket
import ipaddress
import sys
def main():
    print("Welcome to the Server")
    n = len(sys.argv)
    if n != 3:
        print("Invalid number of arguments")
        print("Example Python Server.py <IPv4_Address> <Port_Number>")
        return

    ip = sys.argv[1]
    port = int(sys.argv[2]) #this assigns the port number

    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this is how you make a socket in python
        print("Socket Successfully Created")
        soc.bind((ip, port)) #you need to bind the socket to an ip address
        print("Socket successfully binded on ip address: " + str(ip) + " port: " + str(port))
        soc.listen(1)
        print("Listening on port: " + str(port))
        conn, addr = soc.accept()
        print("Connection Established with " + str(addr))
        while True:
            data = conn.recv(1024)
            
            print("Received from client: " + str(data.decode('utf-8')))
            if data.decode('utf-8') == "stop":
                print("Stop notion recieved stopping server")
                break

    except socket.error as err:
        print(err)
        return

    finally:
        soc.close()
main()