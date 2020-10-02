import socket  
#import Socket for TCP-IP connection 
#change by Jeevan0023


print("Multiple comment lines skipped by Bishal")

if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host =(input("Enter server ip: "))
    port = int(input("Enter port: "))
    print("Multiple comment lines skipped by Bishal")

    serversocket.connect((host, port))
    filename = "recieved"
    with open(filename, 'wb') as f:
        while True:
            print("Recieving Data")
            data = serversocket.recv(1024)
            if not data:
                break
            f.write(data)
        f.close
        print("the program is good")
        print("changes by neha")
