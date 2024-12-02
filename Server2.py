import socket
import threading
import time

class Cliente:
    name = ""
    conn = None
    addr = None

def clientthread(conn, addr):
    conn.send(bytes(f"Bienvenido {addr}\n", 'utf-8'))
    while True:
        try:
            message = conn.recv(BUFFER_SIZE)  # Bloquea hasta recibir un mensaje
            if message:
                msg = message.decode('utf-8')
                print(f"<{addr[0]}> {msg}")
                
                # Comandos especiales
                if msg.startswith('<name>'):
                    setName(conn, msg.removeprefix('<name>'))
                elif msg.startswith('<lista'):
                    enviar_clientes(conn)
                elif msg.startswith('<private:'):
                    mensaje_privado(conn, msg)
                elif msg.startswith('<group:'):
                    mensaje_grupo(conn, msg)
                elif msg.startswith('<create_group:'):
                    crear_grupo(conn, msg.removeprefix('<create_group:').strip())
                elif msg.startswith('<command>'):
                    broadcast(msg + '\n', conn)
                elif msg.startswith('<add_to_group:'):
                    añadir_grupo(conn, msg.removeprefix('<add_to_group:').strip())
                else:
                    # Mensaje general
                    message_to_send = f"<{getName(conn)}> {msg}\n"
                    broadcast(message_to_send, conn)
            else:
                remove(conn)
                print("SE DESCONECTA")
                break
        except Exception as e:
            print(f"Error en hilo de cliente: {e}")
            break

def setName(connection, name: str):
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

def buscar_usuario(name: str):
    for client in list_of_clients:
        if client.name == name:
            return client
    return None

# Funciones de mensajes privados
def mensaje_privado(conn, msg: str):
    try:
        _, destinatario, mensaje = msg.split(':', 2)
        destinatario = destinatario.strip()
        mensaje = mensaje.strip()
        cliente_destino = buscar_usuario(destinatario)
        if cliente_destino:
            cliente_destino.conn.send(bytes(f"[Privado de {getName(conn)}]: {mensaje}\n", 'utf-8'))
        else:
            conn.send(bytes("Usuario no encontrado.\n", 'utf-8'))
    except ValueError:
        conn.send(bytes("Formato incorrecto para mensaje privado.\n", 'utf-8'))

# Grupos
grupos = {}

def crear_grupo(conn, group_name: str):
    if group_name in grupos:
        conn.send(bytes(f"El grupo '{group_name}' ya existe.\n", 'utf-8'))
    else:
        grupos[group_name] = []
        conn.send(bytes(f"Grupo '{group_name}' creado.\n", 'utf-8'))

def añadir_grupo(conn, command: str):
    try:
        group_name, destinatario = command.split(':', 1)
        group_name = group_name.strip()
        destinatario = destinatario.strip()
        cliente_destino = find_client_by_name(destinatario)
        if group_name in grupos and cliente_destino:
            grupos[group_name].append(cliente_destino)
            conn.send(bytes(f"Usuario {destinatario} añadido al grupo '{group_name}'.\n", 'utf-8'))
        else:
            conn.send(bytes("Grupo o usuario no encontrado.\n", 'utf-8'))
    except ValueError:
        conn.send(bytes("Formato incorrecto para añadir al grupo.\n", 'utf-8'))

def mensaje_grupo(conn, msg: str):
    try:
        _, group_name, mensaje = msg.split(':', 2)
        group_name = group_name.strip()
        mensaje = mensaje.strip()
        if group_name in grupos:
            for cliente in grupos[group_name]:
                if cliente.conn != conn:
                    cliente.conn.send(bytes(f"[Grupo {group_name} - {getName(conn)}]: {mensaje}\n", 'utf-8'))
        else:
            conn.send(bytes(f"El grupo '{group_name}' no existe.\n", 'utf-8'))
    except ValueError:
        conn.send(bytes("Formato incorrecto para mensaje de grupo.\n", 'utf-8'))
        
def enviar_clientes(conn):
    """Enviar la lista de usuarios conectados al cliente que lo solicitó."""
    client_names = [client.name for client in list_of_clients if client.name]
    response = "<list_response>" + ",".join(client_names) + "</list_response>"
    try:
        conn.send(bytes(response, 'utf-8'))
    except Exception as e:
        print(f"Error enviando la lista de clientes: {e}")

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 3003
    BUFFER_SIZE = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(100)
    list_of_clients = []
    print(f"Escuchando conexiones en: {(host, port)}")
    try:
        while True:
            conn, addr = server.accept()
            nuevo_cliente = Cliente()
            nuevo_cliente.conn = conn
            nuevo_cliente.addr = addr
            list_of_clients.append(nuevo_cliente)
            print(f"Cliente conectado: {addr}")
            threading.Thread(target=clientthread, args=(conn, addr)).start()
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        for client in list_of_clients:
            client.conn.close()
        server.close()
    print("Conexión terminada.")
