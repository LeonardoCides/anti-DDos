import socket
import threading
import time

class MiniFirewall:
    def __init__(self, port=8080, max_requests=5):
        self.port = port
        self.max_requests = max_requests
        self.ip_history = {} 
        
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(('0.0.0.0', port))

    def handle_client(self, conn, addr):
        ip = addr[0]
        current_time = time.time()

      
        if ip not in self.ip_history or (current_time - self.ip_history[ip]['last_access'] > 10):
            self.ip_history[ip] = {'count': 1, 'last_access': current_time}
        else:
            self.ip_history[ip]['count'] += 1
            self.ip_history[ip]['last_access'] = current_time

       
        if self.ip_history[ip]['count'] > self.max_requests:
            print(f"⚠️ BLOCK: {ip} excedeu o limite de requisições!")
            conn.send(b"HTTP/1.1 429 Too Many Requests\n\nRate limit exceeded.")
            conn.close()
            return

        
        try:
            req = conn.recv(1024)
            if len(req) > 1024:
                conn.send(b"HTTP/1.1 400 Bad Request\n\nPayload too large.")
            else:
                print(f"✅ OK: Requisição aceita de {ip}")
                conn.send(b"HTTP/1.1 200 OK\n\nConnection successful.")
        finally:
            conn.close()

    def listen(self):
        self._sock.listen(100)
        print(f"🚀 Firewall rodando na porta {self.port}...")
        
        while True:
            conn, addr = self._sock.accept()
           
            client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == '__main__':
    firewall = MiniFirewall(port=8080, max_requests=5)
    firewall.listen()
