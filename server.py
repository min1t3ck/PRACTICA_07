import socket
import threading
import time
import pickle

class Cliente:
    name = ""
    conn = None
    addr = None

def clientthread(conn, addr):

    try:
        conn.send(bytes(f"Bienvenido {addr}\n", 'utf-8'))
        while True:
            try:
                message = conn.recv(BUFFER_SIZE)
                if message:
                    print(f"<{addr[0]}> {message}")
                    msg = message.decode('utf-8')

                    # Procesar mensajes especiales
                    if msg.startswith('<name>'):
                        setName(conn, msg.removeprefix('<name>'))

                    elif msg.startswith('<command>'):
                        broadcast(msg + '\n', conn)
                    elif msg.startswith('<Lista>'):
                        EnviarLista()
                    else:
                        # Reenviar el mensaje a otros clientes
                        message_to_send = f"<{getName(conn)}> {msg}\n"
                        broadcast(message_to_send, conn)
                else:
                    print(f"Cliente desconectado: {addr}")
                    remove(conn)
                    break
                EnviarLista()
            except ConnectionResetError:
                print(f"Cliente desconectado abruptamente: {addr}")
                remove(conn)
                break
    except Exception as e:
        print(f"Error en el hilo del cliente {addr}: {e}")
    finally:
        conn.close()

def setName(connection, name:str):
    for client in list_of_clients:
        if client.conn == connection:
            client.name = name
            break

def getName(connection) -> str:
    for client in list_of_clients:
        if client.conn == connection:
            return client.name
    return ""

def broadcast(message, connection):
    for client in list_of_clients:
        if client.conn != connection:
            try:
                client.conn.send(bytes(message, 'utf-8'))
            except:
                client.conn.close()
                remove(client)

def remove(connection):
    for client in list_of_clients:
        if client.conn == connection:
            list_of_clients.remove(client)
            break
         # Enviar lista actualizada tras desconexión
    EnviarLista()

def EnviarLista():
    lista_nombres = [client.name if client.name else str(client.addr) for client in list_of_clients]

    for client in list_of_clients:
        try:
            client.conn.send(pickle.dumps(lista_nombres))
        except:
            client.conn.close()
            remove(client)

if __name__ == "__main__":
    #host = socket.gethostname()  # Esta función nos da el nombre de la máquina
    host = "0.0.0.0"
    port = 3003
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    # Creamos un socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(100)  # Escuchamos hasta 100 clientes
    list_of_clients = []  # Lista de clientes conectados
    print(f"Escuchando conexiones en: {(host, port)}")
    try:
        while True:
            conn, addr = server.accept()
            nuevo_cliente = Cliente()
            nuevo_cliente.conn = conn
            nuevo_cliente.addr = addr
            #list_of_clients.append(conn)  # Agregamos a la lista de clientes
            list_of_clients.append(nuevo_cliente)  # Agregamos a la lista de clientes
            print(f"Cliente conectado: {addr}")
            threading.Thread(target=clientthread, args=(conn, addr)).start()
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        conn.close()
        server.close()
    print("Conexión terminada.")