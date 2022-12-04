import socket

Buffer_size = 2048
# specify the port to make the connnection through it
PORT  = 12340
# get the host public ip address
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
ADDRESS = (SERVER,PORT)
# using tcp connection
client_tcp  = socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
client_tcp.connect(ADDRESS)
DISCONNECT_MESSAGE = "!DISCONNECT"
def send(data):
    message = data.encode("UTF-8")
    msg_len = len(message)
    send_len = str(msg_len).encode("UTF-8")
    send_len += b' '*(Buffer_size-len(send_len))
    client_tcp.send(send_len)
    client_tcp.send(message)
    ack = client_tcp.recv(Buffer_size).decode("UTF-8")
    if bool(ack):
        print("MSG sent Successfully!")
    else:
        print("Msg lost!!")
    msg_received = client_tcp.recv(Buffer_size).decode("UTF-8")    
    print(f"[RECEIVED]: {str(msg_received)}")        
 
 
while True:
    msg = input("Enter your message here: ")
    send(msg)
    
    
    

# send(DISCONNECT_MESSAGE)    
