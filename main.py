"""
  ____                   _ _               __     ____   
 |  _ \            /\   | (_)             / /    / /\ \  
 | |_) |_   _     /  \  | |_  ___  _   _ / /    / /  \ \ 
 |  _ <| | | |   / /\ \ | | |/ _ \| | | < <    / /    > >
 | |_) | |_| |  / ____ \| | | (_) | |_| |\ \  / /    / / 
 |____/ \__, | /_/    \_\_|_|\___/ \__,_| \_\/_/    /_/  
         __/ |                                           
        |___/                                            

  _______                  _       _               _______   _      _           _    __      ____  __ 
 |__   __|                | |     | |             |__   __| | |    | |         | |   \ \    / /_ |/_ |
    | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __     | | ___| | ___| |__   ___ | |_   \ \  / / | | | |
    | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|    | |/ _ \ |/ _ \ '_ \ / _ \| __|   \ \/ /  | | | |
    | | | | (_| | | | \__ \ | (_| | || (_) | |       | |  __/ |  __/ |_) | (_) | |_     \  /   | |_| |
    |_|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|       |_|\___|_|\___|_.__/ \___/ \__|     \/    |_(_)_|
                                                                                                                                                                                                                                           
"""
# IMPORTATION DES MODULES
import os
import requests
import telebot
from dotenv import load_dotenv
import re
import yaml

class TranslationBot:
    def __init__(self):

        # CHARGER DEPUIS ENV
        load_dotenv()

        # INFOS DU BOT
        self.telegram_api_token = os.getenv('TELEGRAM_API_TOKEN')
        self.bot = telebot.TeleBot(self.telegram_api_token)
        self.bot_info = self.bot.get_me()
        self.bot_name, self.bot_id, self.bot_username = (
            self.bot_info.first_name,
            self.bot_info.id,
            self.bot_info.username,
        )

        # YAML - LANGUES
        with open("lang.yml", "r", encoding="utf-8") as file:
            self.messages = yaml.safe_load(file)

    # TRADUCTION - API
    def translate_text(self, text, source_lang, target_lang):
        body = {"de": source_lang, "a": target_lang, "text": text}
        response = requests.post('https://ctranslator.vercel.app/api', json=body)
        if response.status_code == 200:
            return response.json().get('reponse', 'Une erreur s\'est produite lors de la traduction.')
        else:
            return 'Une erreur s\'est produite lors de la traduction.'
    
    # LANGUE PAR DEFAUT
    def get_message(self, message_key, user_language='fr'):
        default_language = 'fr'
        return self.messages.get(user_language, {}).get(
            message_key,
            self.messages.get(default_language, {}).get(message_key, ''),
        )

    # COMMANDE START
    def start(self):
        @self.bot.message_handler(commands=['start'])
        def welcome_message(message):
            user_language_code = message.from_user.language_code
            welcome_message = self.get_message('welcome', user_language_code)
            self.bot.send_chat_action(chat_id=message.chat.id, action="typing")
            self.bot.reply_to(message, welcome_message, parse_mode='Markdown')

        # COMMANDE /EN & /FR
        @self.bot.message_handler(commands=['fr', 'en'])
        def translate_command(message):
            self.bot.send_chat_action(chat_id=message.chat.id, action="typing")
            command, *text = message.text.split(maxsplit=1)
            if not text:
                message_prompt = self.get_message('enter_text', message.from_user.language_code)
                self.bot.reply_to(message, message_prompt)
                return
            text = text[0]
            source_lang, target_lang = (
                ("en", "fr") if command == "/fr" else ("fr", "en")
            )
            response = self.translate_text(text, source_lang, target_lang)
            self.bot.reply_to(message, response)
        
        # FONCTION GROUPE - MENTION
        @self.bot.message_handler(func=lambda message: message.reply_to_message is not None)
        def translate_reply(message):
            original_text = message.reply_to_message.text
            match = re.search(
                fr'@{re.escape(self.bot_username)}\s+(fr|en)\b',
                message.text,
                re.IGNORECASE,
            )
            if match:
                self.bot.send_chat_action(chat_id=message.chat.id, action="typing")
                command = match.group(1).lower()
                source_lang, target_lang = (
                    ("en", "fr") if command == "fr" else ("fr", "en")
                )
                response = self.translate_text(original_text, source_lang, target_lang)
                self.bot.reply_to(message.reply_to_message, response)
        
        # MESSAGE INFO
        print(
            f"Le bot '{self.bot_name}' (ID: {self.bot_id}) avec le nom d'utilisateur @{self.bot_username} a démarré avec succès."
        )
        self.bot.infinity_polling()


if __name__ == "__main__":
    translation_bot = TranslationBot()
    translation_bot.start()
