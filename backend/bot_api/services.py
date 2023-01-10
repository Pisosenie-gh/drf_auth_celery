import requests
token="5953506929:AAELqHGJICkc-HvDXVbQx7n_-AWFVA3g0mU"

def send(chat_id, text):
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

