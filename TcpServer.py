import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9001)
print("[+] Server IP {} | Port {}".format(server_address[0],server_address[1]))

sock.bind(server_address)

sock.listen(1)

while True:
    print('[+] Waiting for a client connection')

    connection, client_address = sock.accept()
    print('[+] Connection from', client_address)

    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(128)
            print('received "%s"' % data)
            if data:
                continue
                # print('sending data back to the client')
                # connection.sendall(data)
            else:
                print('no more data from', client_address)
                break

    finally:
        connection.close()

