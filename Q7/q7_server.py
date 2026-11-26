import socket
import threading
import os


HOST = "127.0.0.1"
PORT = 5000


def receive_file(conn):

    filename = conn.recv(1024).decode()

    if not filename:
        return

    conn.sendall(b"READY")

    size_data = conn.recv(1024).decode()

    file_size = int(size_data)

    received = 0

    with open("received_" + os.path.basename(filename), "wb") as file:

        while received < file_size:

            data = conn.recv(4096)

            if not data:
                break

            file.write(data)

            received += len(data)

    print(
        f"File received: {filename}"
    )

    print(
        f"Bytes received: {received}"
    )


def chat(conn):

    while True:

        message = conn.recv(1024).decode()

        if not message:
            break

        print("Client:", message)

        if message.lower() == "exit":
            break

        reply = input("Server: ")

        conn.sendall(reply.encode())

        if reply.lower() == "exit":
            break


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))

server.listen(1)

print(
    f"Server listening on {HOST}:{PORT}"
)

conn, address = server.accept()

print(
    "Connected by:",
    address
)

while True:

    choice = conn.recv(1024).decode()

    if not choice:
        break

    if choice == "FILE":

        receive_file(conn)

        conn.sendall(
            b"FILE_RECEIVED"
        )

    elif choice == "CHAT":

        chat(conn)

        break

    elif choice == "EXIT":

        break


conn.close()
server.close()

print("Server closed.")