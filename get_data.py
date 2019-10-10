import socket

class get_data:

    '''Connects to a socket of oscyloscope and sends STARTBIN request'''

    start = str("STARTBIN").encode()
    receiving_len = 2048
    o_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buf = bytearray()
    message_len = int()
    header_len = 12

    def get(self, ip, port):
        self.o_socket.connect((ip, port))
        self.o_socket.send(self.start)
        self.buf.extend(self.o_socket.recv(self.receiving_len))
        self.message_len = int.from_bytes(self.buf[:2], "little") + self.header_len
        while len(self.buf) < self.message_len:
            self.buf.extend(self.o_socket.recv(self.receiving_len))

if __name__ == '__main__':
    get_data.get(get_data, "192.168.10.72", 3000)
    print(get_data.buf)
