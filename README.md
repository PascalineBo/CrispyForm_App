# Crispy_App
Entraînement à l'utilisation de **webpack-boilerplate** (https://python-webpack-boilerplate.readthedocs.io/en/latest/) et crispy forms

Grâce au wepinaire de **[Place Python](https://placepython.fr/)**

(dépôt de code original: https://github.com/placepython/wepynaire-django-crispy-forms-20230110?sc=72554853702a5afd9cefccfae385683b3b283f47)

Pour utiliser cette app:



## Comment installer cette Appli sur votre ordinateur:
Requis: téléchargez **[Python 3.10](https://www.python.org/downloads/)** et **[NodeJS](https://nodejs.org/fr/download/)**
<ol>
  <li> Avec les commandes du terminal, positionnez-vous sur le dossier dans lequel vous souhaitez installer l'Appli</li>

  <li> pour importer les fichiers de ce repository, tapez la commande git:

`git clone https://github.com/MargueriteEffren/Crispy_App.git`</li>

  <li> positionnez-vous dans le répertoire Crispy_App:
    
- `cd Crispy_App` </li>
  
  <li>  créez votre dossier d'environnement virtuel:

- `mkdir .venv`
- `pip install pipenv`
</li>

  <li> puis installez les packages requirements du projet à l'aide des commandes:

- `pipenv install django`
- `pipenv install python-webpack-boilerplate`
- `pipenv install crispy-bootstrap5`
- `cd frontend` puis `npm install`</li>
- `npm build start`
</li>

<li> appuyez sur Ctr + C pour sortir

  </ol>


## Comment utiliser l'Appli:
<ol>
  <li> avec votre terminal, positionnez vous dans le dossier dans lequel vous avez installé l'Appli</li>
  
  <li>
    
`cd Crispy_App\frontend`
  puis  
    
- `npm run build` pour compiler le code front
    
  </li>
   <li> 
    
- `Ctrl + C` puis à la question du terminal "Terminer le programme de commandes (O/N) ? " répondez `N`</li>

  <li> retournez à la racine de Crispy_App  `cd ..`</li>

  <li> activez l'environnement virtuel à l'aide des commandes du terminal:
    
- `pipenv shell`
    
</li>
  <li> ensuite tapez la commande 

`python manage.py runserver`

pour exécuter le serveur de développement</li>

<li> entrez dans votre navigateur l'adresse:

http://127.0.0.1:8000/</li>
    </ol>
