# Test Technique Data Engineering - Acme

##  Description

Ce projet met à jour les numéros de série des badges employés dans la base de données Acme à partir d'un fichier CSV.

##  Outils qui doivent etre préinstallés

- Python 3
- MySQL
- Docker 

##  Installation

### 

1. Clonage du repository

 ```bash
 $ git clone
```
Aller dans le dossier et creer un environnement virtuel

 ```bash
 $ cd archives
 $ python -m venv venv
 $ source venv/bin/activate
```
2. Lancement de la base de données MySQL avec Docker Compose :
  ```bash
  $ docker-compose up -d
  ```
3. Installez les dépendances Python :

```bash
  pip install -r requirements.txt
  ```

## Utilisation

Exécution du script

```bash
  python update_serial_numbers.py
```
![Texte alternatif](chemin/vers/image.png)


## Configuration
Le script utilise par défaut les paramètres de connexion suivants :

* Host : localhost
* User : root
* Password : root
* Database : acme


## Fonctionnement
Le script effectue les opérations suivantes :

* Chargement du CSV : Lecture du fichier updated_serial_numbers.csv avec pandas
* Connexion à la base : Établissement de la connexion MySQL
* Mise à jour : Pour chaque ligne du CSV, mise à jour du serial_number correspondant à l'employee_id
* Vérification : Contrôle que la mise à jour a bien été effectuée
* Validation : Commit des changements et fermeture de la connexion

## Validation
Le script inclut une vérification automatique qui :

* Vérifie que chaque mise à jour a bien été appliquée
* Affiche un message de confirmation ou d'erreur pour chaque employé traité