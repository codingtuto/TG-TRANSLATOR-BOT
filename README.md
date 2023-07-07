
# Bot Traducteur

Ce projet est un Bot Traducteur utilisant l'API CodingTranslator pour traduire des textes entre l'anglais et le français et vice versa.

## Démonstration

- [@en_frbot](https://t.me/en_frbot)

## Installation

Clonez ce dépôt Git sur votre machine locale :

```bash
  https://github.com/codingtuto/TG-TRANSLATOR-BOT/
```

Renommez le fichier `.env.example` en `.env`.
Remplacez `VOTRE_TOKEN_API_ICI` par votre jeton d'API dans le fichier `.env` : comme ceci
```bash
  TELEGRAM_API_TOKEN=5674:XXXXXXXXXXXXXXXXXXXXX
```

Installez les dépendances en exécutant : Vous devez etre sur le dossier du bot `cd TG-TRANSLATOR-BOT`:

```bash
  pip install -r requirements.txt
```
## Utilisation

Maintenant que vous avez configuré le projet, vous pouvez l'utiliser pour traduire des textes. Exécutez le script principal avec la commande suivante :
```bash
  python main.py
```

    
## Commandes
Le Bot Traducteur prend en charge deux commandes :

`/fr <texte>`: Traduit le texte de l'anglais vers le français.

`/en <texte>` : Traduit le texte du français vers l'anglais.


## Technologies

**Framework:** Telebot

**Langage:** Python


## Auteur

- [@codingtuto](https://www.github.com/codingtuto)

## Star History

<a href="https://github.com/codingtuto/TG-TRANSLATOR-BOT/">
        <img width="500" alt="Star History Chart" src="https://api.star-history.com/svg?repos=codingtuto/TG-TRANSLATOR-BOT&type=Date">
      </a> 
