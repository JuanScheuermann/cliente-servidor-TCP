import socket
import threading

class Server:

    def __init__(self):
        
        self._hostname = socket.gethostname();
        self._ip = socket.gethostbyname(self._hostname);
        self._port = 9998;
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    def iniciar(self):

        #Le decimos al servidor que escuche en esta direccion
        self._server.bind((self._ip, self._port));

        #El servidor empieza a escuchar
        self._server.listen();
    
        print(f"[*] corriendo servidor en: {self._ip}:{self._port}");

        while True:
                #cuando un cliente se conecta recivimos el socket del cliente en la variable socket
                #y las esepcificaciones de la conexion remota en la variable address
                socket, address = self._server.accept();

                print(f"Aceptando conexion de: {address[0]}:{address[1]}");
                client_thread = threading.Thread(target=self.handle_client, args=(socket,));
                client_thread.start();
    
    
    @classmethod
    def handle_client(self, client_socket):

        with client_socket as socket:
            #Request del cliente en un buffer de 1024 bits
            request = socket.recv(1024);
            print(f"[*] Request: {request.decode("utf-8")}");
            socket.send(b"solicitud recivida");
