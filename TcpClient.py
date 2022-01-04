
import socket


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.223.31.201', 9001)

print('[+] Connecting to %s Port %s' % server_address)
sock.connect(server_address)

try:
    message = 'BUZZER_SLBR-041_PRESSED'
    print('[+] Sending "%s"' % message)
    sock.sendall(message.encode('latin-1'))

    # # Look for the response
    # amount_received = 0
    # amount_expected = len(message)
    #
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     print
    #     '[+] Received "%s"' % data

finally:
    sock.close()
