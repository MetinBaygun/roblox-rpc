from pypresence import Presence
import time
import requests
from config import *

client_id = "1395704825764905123" # degistirmemeniz önerilir.


user_info = requests.get("https://users.roblox.com/v1/users/7006004968")
username = user_info.json().get("name", "Bilinmiyor")


cookie = '.ROBLOSECURITY=token'
headers = {
    'Cookie': cookie,
    'Content-Type': 'application/json'
}

data = {
    "userIds": [7006004968]
}

client_id = "1395704825764905123"  
response = requests.post("https://presence.roblox.com/v1/presence/users", headers=headers, json=data)

veri = response.json()
bilgi = veri["userPresences"][0]
oyun = bilgi.get("lastLocation", "Oyunda değil")
oyunid = bilgi.get("placeId", "Oyunda değil")

kullaniciId = "7006004968" 

avatar_api = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={kullaniciId}&size=150x150&format=Png&isCircular=true"
avatar_response = requests.get(avatar_api)
avatar_url = avatar_response.json()["data"][0]["imageUrl"]



if response.status_code == 200:
    info = response.json()["userPresences"][0]



RPC = Presence(client_id)
RPC.connect()

start_time = time.time()
presence_type = bilgi.get("userPresenceType", 0)


print("RPC çalışıyor... Yapan:Berlin")
print("presence_type:", presence_type)

presence_type = bilgi.get("userPresenceType", 0)

while True:

    response = requests.post("https://presence.roblox.com/v1/presence/users", headers=headers, json=data)
    veri = response.json()
    bilgi = veri["userPresences"][0]
    presence_type = bilgi.get("userPresenceType", 0)
    oyun = bilgi.get("lastLocation", "Oyunda değil")
    avatar_api = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={kullaniciId}&size=150x150&format=Png&isCircular=true"
    avatar_response = requests.get(avatar_api)
    avatar_url = avatar_response.json()["data"][0]["imageUrl"]

    try:
        oyun_api = f"https://thumbnails.roblox.com/v1/places/gameicons?placeIds={oyunid}&size=512x512&format=Png"
        oyun_response = requests.get(oyun_api)
        oyun_url = oyun_response.json()["data"][0]["imageUrl"]
    except KeyError:
        oyun_url = "https://www.roblox.com/favicon.ico"  # Fallback image if the game icon is not found

    if presence_type == 2:
        print("if tetiklendi")
        RPC.update(
            details=f"{username} (ID: {kullaniciId})",    
            state=f"Playing {oyun}",
            start=start_time,
            large_image=f"{oyun_url}",
             large_text=f"{oyun}",
             small_image=f"{avatar_url}",
            small_text="TanerTTarlaci"
        )

    else:
        print("Kullanıcı oyunda değil veya bilgileri alınamadı.")
        time.sleep(15)
