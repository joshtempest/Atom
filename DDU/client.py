import socket #Importerer et python library

HEADER = 64 #Sætter en værdi til en variabel vi skal bruge senere
PORT = 5050 #Sætter hvilken port computeren skal bruge til clienten
FORMAT = 'utf-8' #Encrypteringskode
DISCONNECT_MESSAGE = "!DISCONNECT" #For at sige til serveren at clienten er disconnectet
SERVER = "10.107.163.11" #serverens IP adresse
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) #Connecter til serveren

def send(msg): #Definerer hvordan man sender en bedsked
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #print(client.recv(2048).decode(FORMAT)) #Er fjernet da det skabte problemer for vores udvidet kode

send("Hello World!") #Sender første bedsked

while True:
    M = input("")
    send(M)
    if M == "!exit":
        send(DISCONNECT_MESSAGE)
        connected=False
        exit()
