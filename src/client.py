import socket

nombre_host = "www.google.com";
puerto_host = 80;

#CREAR EL SOCKET DEL CLIENTE
#AF_INET es la familia de direcciones de internet ipv4
#SOCK_STREAM es el protocolo TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

#Establecemos una conexion con el cliente pasando una tupla con su nombre y puerto
client.connect((nombre_host, puerto_host));

#Enviamos una coleccion de bytes.
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n");

response = client.recv(4096)
print(response.decode());
