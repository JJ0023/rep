import socket                   

if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host =str(input("Enter server ip: "))
    port = int(input("Enter port: "))

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
