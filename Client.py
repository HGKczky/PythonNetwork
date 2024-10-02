import socket
import sys
def main():
    print("Welcome to the client")
    n = len(sys.argv)
    if n != 3:
        print("Invalid number of arguments")
        print("Example Python Client.py <IPv4_Address> <Port_Number>")
        return

    ip = sys.argv[1]
    port = int(sys.argv[2]) #this assigns the port number

    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this is how you make a socket in python
        soc.connect((ip, port)) #connects to this client on port 8080
        print("Connection Established with the server " + str(ip))
        while True:
            message = input("Enter data: ")
            soc.send(message.encode('utf-8')) #send the message to the server first
            if message == "stop":
                print("Stopping client...")
                break

    except socket.error as err:
        print(err) #print the error if none of those works
        return

    finally:
        soc.close() #makes sure the socket is closed
main()
