import socket
import argparse


def main(host_name, host_port):
    nombre_host = host_name;
    puerto_host = host_port;

    #CREAR EL SOCKET DEL CLIENTE
    #AF_INET es la familia de direcciones de internet ipv4
    #SOCK_STREAM es el protocolo TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    #Establecemos una conexion con el cliente pasando una tupla con su nombre y puerto
    client.connect((nombre_host, puerto_host));

    #Enviamos una coleccion de bytes.
    client.send(b"Hola desde el cliente");

    #Recivimos una respuesta por medio del metodo recv al cual le pasamos
    #el numero de bits que tendra el buffer (4096)
    response = client.recv(4096)

    #Decodificamos la respuesta ya que si la imprimimos como si nada
    #veremos puros bytes
    print(response.decode("utf-8"));

if __name__ == "__main__":
    #configurando los argumentos del programa cliente
    parser = argparse.ArgumentParser(description="Esta herramienta realiza una solicitud " + 
                                     "por medio de TCP");

    parser.add_argument("--hostname",type=str,
                        help="El nombre del host al que se busca conectar");

    parser.add_argument("--port",type=int,
                        help="Numero de puerto para realizar la conexion al servidor");

    args = parser.parse_args();
    
    main(
        host_name=args.hostname,
        host_port=args.port
    );
