import socket
import threading

class PublisherServer:
    def __init__(self):
        self.host = 'localhost'  # Server's IP address
        self.port = 5555         # Port number
        self.subscribers = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def run(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"New connection from {addr}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        self.subscribers.append(client_socket)
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Received message: {message}")
                self.notify_subscribers(message)
            except Exception as e:
                print(f"Error: {e}")
                break
        client_socket.close()
        self.subscribers.remove(client_socket)

    def notify_subscribers(self, message):
        for subscriber in self.subscribers:
            try:
                subscriber.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending to subscriber: {e}")
                self.subscribers.remove(subscriber)

if __name__ == "__main__":
    server = PublisherServer()
    server.run()
