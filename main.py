"""
  ____                   _ _               __     ____   
 |  _ \            /\   | (_)             / /    / /\ \  
 | |_) |_   _     /  \  | |_  ___  _   _ / /    / /  \ \ 
 |  _ <| | | |   / /\ \ | | |/ _ \| | | < <    / /    > >
 | |_) | |_| |  / ____ \| | | (_) | |_| |\ \  / /    / / 
 |____/ \__, | /_/    \_\_|_|\___/ \__,_| \_\/_/    /_/  
         __/ |                                           
        |___/                                            

  _______                  _       _               _______   _      _           _    __      ____ 
 |__   __|                | |     | |             |__   __| | |    | |         | |   \ \    / /_ |
    | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __     | | ___| | ___| |__   ___ | |_   \ \  / / | |
    | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|    | |/ _ \ |/ _ \ '_ \ / _ \| __|   \ \/ /  | |
    | | | | (_| | | | \__ \ | (_| | || (_) | |       | |  __/ |  __/ |_) | (_) | |_     \  /   | |
    |_|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|       |_|\___|_|\___|_.__/ \___/ \__|     \/    |_|
                                                                                                  
                                                                                                  
"""
import os
import requests
import telebot
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer le jeton d'API Telegram à partir de la variable d'environnement
telegram_api_token = os.getenv('TELEGRAM_API_TOKEN')

# Créer un objet TeleBot avec le jeton d'API Telegram
bot = telebot.TeleBot(telegram_api_token)

# Fonction de traduction
def traduire_texte(texte, de, a):
    body = {
        "de": de,
        "a": a,
        "text": texte
    }

    # Envoyer la requête à l'API de traduction
    response = requests.post('https://codingtranslator.onrender.com/api', json=body)

    if response.status_code == 200:
        # Récupérer la réponse de l'API de traduction
        reponse = response.json()['reponse']
        return reponse
    else:
        return 'Une erreur s\'est produite lors de la traduction.'

# Commande /start
@bot.message_handler(commands=['start'])
def afficher_message_bienvenue(message):
    message_bienvenue = '''👋 Bienvenue ! Je suis votre *traducteur Anglais Francais* 🌍
*Voici les principales commandes que je propose :*
    🇺🇸 `/fr hello this is a test` - Traduire le texte en anglais vers francais.
    🇫🇷 `/en salut je suis un test` - Traduire le texte en francais vers anglais.

*Vous pouvez compter sur moi pour des traductions rapides et précises. 🚀*

📦 *Le code source de ce bot est open source et peut être consulté sur ce dépôt Git :* [Lien vers le code source](https://github.com/codingtuto/TG-TRANSLATOR-BOT/)

*🆚 Version : 1.0.0 - By @A_liou*
    '''
    bot.send_chat_action(chat_id=message.chat.id, action="typing")
    bot.reply_to(message, message_bienvenue, parse_mode='Markdown')

# Gérer les commandes de traduction /fr & /en en une seule
@bot.message_handler(commands=['fr', 'en'])
def traduire_texte_commande(message):
    bot.send_chat_action(chat_id=message.chat.id, action="typing")
    commande, texte = message.text.split(maxsplit=1)
    source_lang, target_lang = ("en", "fr") if commande == "/fr" else ("fr", "en")
    reponse = traduire_texte(texte, source_lang, target_lang)
    bot.reply_to(message, reponse)
  
# Répondre aux autres messages
@bot.message_handler(func=lambda message: True)
def repondre_autre(message):
    bot.send_chat_action(chat_id=message.chat.id, action="typing")
    bot.reply_to(message, 'Veuillez utiliser la commande /fr ou /en pour traduire le texte.')

# Lancer le bot
bot.polling()
