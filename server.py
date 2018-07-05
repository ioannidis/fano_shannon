from classes.linear_code import LinearCode
import socket
import json

# https://pymotw.com/2/socket/tcp.html

def main():
    print("\nSERVER ================================================\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('127.0.0.1', 1001)
    print("[INFO] Starting server with address: {}.".format(address))
    sock.bind(address)
    sock.listen(1)

    connection, client_address = sock.accept()
    print("[INFO] Accepted connection from {}.\n".format(client_address))

    try:
        data = connection.recv(1024)
        print("[INFO] Received data from client: {}.\n".format(data.decode("utf-8")))

        json_data = json.loads(data.decode("utf-8"))
        lc = LinearCode()
        res = lc.decode(json_data)

        print("[INFO] Sending data to client: {}.\n".format(res))
        connection.sendall(res.encode("utf-8"))

    finally:
        print("[INFO] Closing connection and socket.\n")
        connection.close()
        sock.close()


if __name__ == "__main__":
    main()
