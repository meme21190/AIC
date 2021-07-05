#!/usr/bin/env python3
# coding: utf-8
###############################
# Création d un faux site web #
# Melissa Rehoudja            #
# 07-2021                     #
# version 3                   #
###############################


#-------------Modules---------#

import os
import webbrowser


os.system('sudo apt install -y git') # Installation de git 
os.system('git clone https://github.com/venkatesannaveen/sample-webapp') # Téléchargement du faux site web
os.system('mkdir projet6') # Création du dosiier projet6
os.system('mv /home/admin1/sample-webapp/ /home/admin1/projet6/sample-webapp/') # Deplacement du faux site web dans le dossier projet6

#------------ Les packages-----#

os.system('sudo apt install -y python3-pip') # Installation de git
os.system('pip3 install click --user') # Installation de click
os.system('pip3 install Flask --user') # Installation de flask
os.system('pip3 install gunicorn --user') # Installation de Gunicorn
os.system('pip3 install itsdangerous --user') # Installation de itsdangerous
os.system('pip3 install Jinja2 --user') # Installation de jinja2
os.system('pip3 install MarkupSafe --user') # Installation de MarkupSafe
os.system('pip3 install Werkzeug --user') # Installation de Werkzeug

#------------------------------#

webbrowser.open('127.0.0.1:5000') # Ouverture du navigateur
os.chdir('/home/admin1/projet6/sample-webapp/') # On se déplace dans le dossier ou se trouve le faux site web
os.system('python3 app.py') # On lance le script du faux site web
os.chdir('/home/admin1/') # On retourne dans le dossier /home de notre utilisateur
os.system('python3 log.py') # On lance le script pour les logs qui va créer un fichier projet6.log



