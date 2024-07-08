import sys, socket
from datetime import datetime


if len(sys.argv) == 2:
    targetip = socket.gethostbyname(sys.argv[1])        #Target ip basically


else:
    targetip = input("Enter Target ")


print("-"*50)
print("Welcome to Silly Scanner you SILLY GOOSE.\n")
print("Scanning target: {}".format(targetip))
print("Scan Started at "+str(datetime.now()))
print("Might take some time :D")
print("-"*50)
print("\n\n")

try:
        for port in range(1,65535):
            ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            results = ss.connect_ex((targetip,port))
            # print("Checking port {}".format(port))
            if results == 0:
                print("{} is open".format(port))
            ss.close()
        
except KeyboardInterrupt:
    print("\n Exiting Program Teehee")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. You really are a silly goose")
    sys.exit()
except socket.error:
    print("Couldn't Connect to server.")
    sys.exit()

print("Scan ended at "+str(datetime.now()))