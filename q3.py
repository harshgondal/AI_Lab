import socket
import re

def client(filename):
    host = 'localhost'  # Server's IP address
    port = 5555         # Port number
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    try:
        # Read the file and convert all text to lowercase
        with open(filename, 'r') as file:
            text = file.read().lower()
        
        # Remove non-alphanumeric characters and split into words
        words = re.findall(r'\b\w+\b', text)
        
        # Initialize an empty dictionary to store word frequencies
        word_counts = {}
        
        # Count frequencies of each word
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        
        # Send each word and its count to the server
        for word in word_counts:
            message = f"{word}: {word_counts[word]}"
            client_socket.send(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server response for '{word}': {response}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client_socket.close()

# Example usage:
if __name__ == "__main__":
    filename = './LICENSE.txt'  # Replace with your file path
    client(filename)
