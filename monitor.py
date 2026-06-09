import os
subprocess
time

DESTINO = "542235590910@s.whatsapp.net"
INTERVALO = 60

def check_msgs():
    res = subprocess.run(["wpp-cli", "unread"], capture_output=True, text=True)
    if "Unread messages" in res.stdout:
        subprocess.run(["wpp-cli", "send", DESTINO, "иш [BOT] Hay clientes esperando en WhatsApp!"])

while True:
    check_msgs()
    time.sleep(INTERVALO)