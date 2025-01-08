import socket
import threading
from queue import Queue

class Scanner:
    def __init__(self, target, ports=None, threads=10):
        self.target = target
        self.ports = ports if ports else list(range(1, 65536))
        self.threads = threads
        self.open_ports = []
        self.services = {}

    def scan(self):
        print(f"\n[+] Scanning {self.target} with {self.threads} threads...")
        q = Queue()
        for port in self.ports:
            q.put(port)

        def worker():
            while not q.empty():
                port = q.get()
                self.scan_port(port)
                q.task_done()

        for _ in range(self.threads):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()

        q.join()

        if self.open_ports:
            print("\n[+] Open Ports Found:")
            for port, service in self.services.items():
                print(f"  {port}/tcp - {service}")
        else:
            print("\n[-] No open ports found.")

    def scan_port(self, port):
        try:
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.settimeout(1)
            if conn.connect_ex((self.target, port)) == 0:
                self.open_ports.append(port)
                try:
                    service = conn.recv(1024).decode('utf-8', 'ignore').strip()
                except:
                    service = "Unknown"
                self.services[port] = service
            conn.close()
        except:
            pass
