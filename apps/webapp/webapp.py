#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask        # Importation du module Flask

webapp = Flask(__name__)        # Création d'une nouvelle application
                                # Flask

@webapp.route("/")    # Chemin depuis la racine du site
                      # http://127.0.0.1:8080/webapp/ (serveur apache)
                      # ou   http://127.0.0.1:5000 (lancé avec python webapp.py)
         
def hello():          # Fonction qui sera appelée lorsque
                      # l'on accède au chemin indiqué dans    
                      # @webapp.route("/")    

     # Code renvoyé au navigateur                          
    return "Hello World from the webapp app! Test git!"  
    
if __name__ == '__main__':
    "Are we in the __main__ scope? Start test server."
    webapp.run()
