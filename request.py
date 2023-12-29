
import requests
url = "https://discord.com/api/v9/channels/{your channel id}/messages"

payload = {"content": "good morning!"}

headers = {
    "Authorization":
"{your authorization token}"
}


response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

