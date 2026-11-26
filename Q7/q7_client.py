import socket
import os


HOST = "127.0.0.1"
PORT = 5000


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

print("Connected to server.")

while True:

    print()
    print("1. Send file")
    print("2. Chat")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        filename = input(
            "Enter file path: "
        )

        if not os.path.isfile(filename):

            print("File not found.")

            continue

        client.sendall(b"FILE")

        client.sendall(
            os.path.basename(filename).encode()
        )

        response = client.recv(1024)

        if response != b"READY":

            print("Server not ready.")

            continue

        file_size = os.path.getsize(filename)

        client.sendall(
            str(file_size).encode()
        )

        with open(filename, "rb") as file:

            while True:

                data = file.read(4096)

                if not data:
                    break

                client.sendall(data)

        response = client.recv(1024)

        print(
            response.decode()
        )

    elif choice == "2":

        client.sendall(b"CHAT")

        while True:

            message = input("You: ")

            client.sendall(
                message.encode()
            )

            if message.lower() == "exit":
                break

            reply = client.recv(1024).decode()

            print(
                "Server:",
                reply
            )

            if reply.lower() == "exit":
                break

        break

    elif choice == "3":

        client.sendall(b"EXIT")

        break

    else:

        print("Invalid choice.")


client.close()

print("Client closed.")