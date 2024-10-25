import socket


class AntiDDOS(object):
    def __init__(self, port=8080):
        self.port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(('0.0.0.0', port))

    def listen(self):
        self._sock.listen(5)
        while 
            conn, addr = self._sock.accept()
            req = conn.recv(1024)
            res = self.process_request(req)
            conn.send(res)

    def process_request(self, req):
       
        if len(req) > 1024:
           
            return b"HTTP/1.1 400 Bad Request\n"
        else:
           
            return b"HTTP/1.1 200 OK\n"

if __name__ == '__main__':
    anti_ddos = AntiDDOS(port=8080)
    anti_ddos.listen()
