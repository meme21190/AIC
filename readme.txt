Les commandes faites sur la vm Debian graphique pour l’installation d’un faux site web, qui compte le nombre de visite.

Il y a juste à lancer le fichier projet6.py avec la commande :
python3 projet6.py

On fait un import os. Ce module fournit une façon portable d'utiliser les fonctionnalités dépendantes du système d'exploitation.
import os

On fait un import webbrowser. Ce module permet d'ouvrir un navigateur
import webbrowser

On install git
os.system('sudo apt install -y git')

On télécharge le faux site web
os.system('git clone https://github.com/venkatesannaveen/sample-webapp')

on va créer le dossier du projet, ici projet6
os.system('mkdir projet6')

On déplace le dossier sample-webapp dans le dossier du projet6
Le nom de l'utilisateur, ici admin1, doit être adapté à votre nom d'utilisateur
os.system('mv /home/admin1/sample-webapp/ /home/admin1/projet6/sample-webapp/')

On install pip 
os.system('sudo apt install -y python3-pip')

On installe le packages requis par le faux site
os.system('pip3 install click --user')
os.system('pip3 install Flask --user')
os.system('pip3 install gunicorn --user')
os.system('pip3 install itsdangerous --user')
os.system('pip3 install Jinja2 --user')
os.system('pip3 install MarkupSafe --user')
os.system('pip3 install Werkzeug --user')

On ouvre notre navigateur sur la page demander
webbrowser.open('127.0.0.1:5000')

On se rend dans le dossier sample-webapp
Le nom de l'utilisateur, ici admin1, doit être adapté à votre nom d'utilisateur
os.chdir('/home/admin1/projet6/sample-webapp/')

On lance le script app.py
os.system('python3 app.py')

Il faut attendre quelques secondes que le script "app.py" se lance.
Il faut rafraichir la page que le navigateur à ouvert pour voir le compteur s'afficher puis il faut cliquer sur actualiser

On retourne dans le dossier ou se trouve le script
os.chdir('/home/admin1/')

On lance le script log.py qui va nous dire si tous c'est bien passer ou non et il créera un fichier de log nommé projet6.log
os.system('python3 log.py')

