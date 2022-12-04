import socket
import threading
import time

class Server:
    Format = "UTF-8"
    DISCONNECT_MESSAGE = "!DISCONNECT"
    Buffer_size = 2048
    PORT  = 12340
    # get the host local ip address
    SERVER = socket.gethostbyname(socket.gethostname())
    # print(SERVER)
    ADDRESS = (SERVER,PORT)
    # using tcp connection
    server_tcp  = socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
    server_tcp.bind(ADDRESS)
    def __init__(self) -> None:
        pass
        
    def __handle_client(self,connection,address)->None:
        print(f'[NEW Connections]: {address} connected')
        connnected = True
        while connnected:
            msg_len = connection.recv(self.Buffer_size).decode(Server.Format)
            if msg_len:
                msg_len = int(msg_len)
                msg = connection.recv(msg_len).decode(Server.Format)
                print(f'[RECEIVED]: {msg}')
                ACk = 'True'
                connection.send(ACk.encode(Server.Format))
                if msg == Server.DISCONNECT_MESSAGE:
                    connnected = False
                reply = input("reply: ")
                connection.send(reply.encode(Server.Format))
        print('Disconnected!')        
        connection.close()  
       
    def start(self):
        # just start to listen if their are any host want to connet 
        print(f'[LISTING] {self.SERVER}')
        self.server_tcp.listen()
        while True:
            connection , address = self.server_tcp.accept()
            thread = threading.Thread(target=self.__handle_client,args=(connection,address))
            thread.start()
            print(f"[Active Connections] ==> {threading.active_count() -1}")

if __name__ == '__main__':
   server= Server()
   server.start()