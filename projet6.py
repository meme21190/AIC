#!/usr/bin/env python3

import os
import webbrowser





os.system('sudo apt install -y git')
os.system('git clone https://github.com/venkatesannaveen/sample-webapp')
os.system('mkdir projet6')
os.system('mv /home/admin1/sample-webapp/ /home/admin1/projet6/sample-webapp/')

os.system('sudo apt install -y python3-pip')
os.system('pip3 install rdflib')
os.system('pip3 install click --user')
os.system('pip3 install Flask --user')
os.system('pip3 install gunicorn --user')
os.system('pip3 install itsdangerous --user')
os.system('pip3 install Jinja2 --user')
os.system('pip3 install MarkupSafe --user')
os.system('pip3 install Werkzeug --user')


webbrowser.open('127.0.0.1:5000'



