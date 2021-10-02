import socket                   

if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host =(input("Set server ip: "))
    port = int(input("Set port: "))

    serversocket.bind((host, port))
    serversocket.listen(5)
    print("Sender is ready and listening")

    clientsocket, address = serversocket.accept()
    print("Reciever " + str(address) + " connected")
    filename = str(input("Enter file name: "))
    #clientsocket.send(filename)

    f = open(filename, 'rb')
    buffer = f.read(1024)
    while(buffer):
        clientsocket.send(buffer)
        buffer = f.read(1024)
    f.close()
    print("Program terminated")


