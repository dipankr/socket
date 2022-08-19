import socket
import argparse
from threading import Thread

# create an object => handler

def handleConnection(conn: socket.socket) -> None:
    # -- sockname - local, peername - remote 
    print(f"Established connection from {conn.getsockname()} to {conn.getpeername()}")

    # step 5, recieve data (max byte)
    data = conn.recv(1024)

    # step 6, send
    updated_data = data.upper()
    conn.sendall(updated_data)

    # step 7, close
    conn.close()
    #sock.close()


def main(host: str, port: int) -> None:

    # step 1, create socker
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # step 2, bind
    sock.bind((host, port))

    # step 3, listen
    sock.listen()
    # -- so far (#3), the socket has only local IP and port 
    print(f"server is listening on {port}")

    while True:
        # step 4, accept
        conn, _ = sock.accept()

        # pass handling to the thread
        thread = Thread(target=handleConnection, args=(conn,))
        thread.start()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socker server')
    parser.add_argument('-p', '--port', help='Port to bind to', required=True, type=int)
    parser.add_argument('-H', '--host', help='Host to bind to', default='127.0.0.1', type=str)

    args = parser.parse_args()
    host, port = args.host, args.port

    main(host, port)

#python server.py --host 127.0.0.1 --port 6000