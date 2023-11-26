
# Bot Traducteur

Ce projet est un Bot Traducteur utilisant l'API CodingTranslator pour traduire des textes entre l'anglais et le français et vice versa.

## Démonstration
![DEMO](https://telegra.ph/file/a1c21de279af8e668afbb.jpg)
- [@en_frbot](https://t.me/en_frbot)

# Journal des modifications
## [Version 1.0.3 ] - 2023-11-26
### Ajouté
- **Support multilingue**: Désormais, le bot peut détecter automatiquement la langue de l'utilisateur en fonction de ses paramètres Telegram. Les langues prises en charge comprennent :
  - Français
  - Anglais
  - العربية (Arabe)
  - Español (Espagnol)
  - Italiano (Italien)
  - Русский (Russe)
![DEMO](https://telegra.ph/file/e5ac3c1fbe910944cf54a.jpg)
## [Version 1.0.2 ] - 2023-07-14
**Mode groupe** (vous pouvez ajouter le bot sur votre groupe en tant que admin pour qu'il effectue des traductions en anglais & francais et vice vers)
**[Ajout]:** Le bot détectera automatiquement son nom d'utilisateur, inutile de saisir le nom d'utilisateur manuellement en réponse à ce [pull request](https://github.com/codingtuto/TG-TRANSLATOR-BOT/commit/5d3770c428a29591d50c196e521a2b3f2f3dd2b9).
## [Version 1.0.1 ] - 2023-06-20
- `en` : Mentionnez le bot suivi de `en` pour traduire du français vers l'anglais.
- `fr` : Mentionnez le bot suivi de `fr` pour traduire de l'anglais vers le français.

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

    
## Utilisation
**Mode privée :**

`/fr <texte>`: Traduit le texte de l'anglais vers le français.

`/en <texte>` : Traduit le texte du français vers l'anglais.

**Mode groupe:**

1. Mentionnez le bot dans un message en utilisant `@en_frbot` suivi de la langue cible (fr ou en) en réponse d'une message.
2. Le bot traduira le message d'origine de l'anglais au français si la langue cible est "fr" ou du français à l'anglais si la langue cible est "en".
3. 
Exemple :

- `@en_frbot en`: Le bot traduira le message de l'anglais au français.
- `@en_frbot fr`: Le bot traduira le message du français à l'anglais.

## Technologies

**Framework:** Telebot

**Langage:** Python

## Auteur

- [@codingtuto](https://www.github.com/codingtuto)

## Star History

<a href="https://github.com/codingtuto/TG-TRANSLATOR-BOT/">
        <img width="500" alt="Star History Chart" src="https://api.star-history.com/svg?repos=codingtuto/TG-TRANSLATOR-BOT&type=Date">
      </a> 

<p align="center"><a href="https://github.com/codingtuto/TG-TRANSLATOR-BOT#"><img src="https://superagi.com/wp-content/uploads/2023/05/backToTopButton.png" alt="Retour en haut" height="29"/></a></p>
