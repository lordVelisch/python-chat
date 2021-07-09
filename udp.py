import argparse
import socket

MAX_SIZE_BYTES = 65535  # Mazimum size of a UDP datagram


def server(port):
    host = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    send_and_receive(s)


def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = input('Enter host to start conversation: ')
    message = input('You: ')
    s.sendto(message.encode('ascii'), (host, port))
    send_and_receive(s)


def send_and_receive(s):
    while True:
        (data, address) = s.recvfrom(MAX_SIZE_BYTES)
        message_recv = data.decode('ascii')
        print('{}: {!r}'.format(address, message_recv))
        new_message = input('You: ')
        s.sendto(new_message.encode('ascii'), address)


if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)
