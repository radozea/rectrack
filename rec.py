import requests
import time

URL = "https://auth.rec.net/account/login"
WEBHOOK = "https://discord.com/api/webhooks/1495593159277940826/oipcO0KtCtEelgv1SVE5kgfkDRhv3N79tSvjDwqFAM4Op2twJIgmcBw4Uz6Jdp9ttsWK"
INTERVAL = 2

print("Monitoring Rec Room login...\n")

was_up = False

while True:
    try:
        r = requests.get(URL, timeout=5)
        is_up = r.status_code < 500
        print(f"🟢 UP ({r.status_code})")
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        is_up = False
        print("🔴 DOWN")

    if is_up and not was_up:
        requests.post(WEBHOOK, json={"content": "<@1430345285384671333> RECROOM IS UP!!!!!"})

    was_up = is_up
    time.sleep(INTERVAL)
