import requests
import time

bot_token = "BOT_TOKEN"
channel_id = "CHANNEL_ID"
messages = { "MESSAGES" }

url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
headers = {"Authorization": bot_token, "Content-Type": "application/json"}
	
	
while True:
    for msg in messages:
        data = {"content": msg}
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code in [200, 201]:
            print(f"Berhasil mengirim pesan: {msg}")
            time.sleep(1)
        else:
            print("Gagal mengirim pesan.")
            
