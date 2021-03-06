
# Projet 5 - Utilisez les données publiques de l'OpenFoodFacts

## Présentation du projet

L'idée est donc de créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, 
les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

## Description du parcours utilisateur

L'utilisateur ouvre le programme, ce dernier lui affiche les choix suivantes:
```
1. Quel aliment souhaitez-vous remplacer?
2. Retrouver mes aliments substitués.
```
L'utilisateur sélectionne 1.   

Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :
* Sélectionnez la catégorie. 
> Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée.

* Sélectionnez l'aliment. 
> Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée.

L'utilisateur sélectionne l'aliment.
>Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.

* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

## Installation & Lancement
### Connection à MySql :
>Pensez à remplacer le chemin complet vers votre dossier source, évidemment.

Ouvrez une invite de commandes :
```
Chemin\Vers\MySQL\MonServeur\bin> mysql -u root -p
Enter password:
```
> TIPS !
> Vous pouvez retrouver le cours sur l'installation et la connexion à MySql [ici.](https://openclassrooms.com/fr/courses/1959476-administrez-vos-bases-de-donnees-avec-mysql/1959969-installez-mysql)  

### Intégralement 

**! Attention** aux sens des "/", sous windows les "\\" ne fonctionnent pas.  
```
mysql> SOURCE C:/Chemin/Vers/Mon/Dossier/app/create_all.sql
```
### Création de la base de données 'Alimentation':
```
mysql> SOURCE C:/Chemin/Vers/Mon/Dossier/app/create_db.sql
```
### Vider & Créer les tables de la base de données
```
mysql> SOURCE C:/Chemin/Vers/Mon/Dossier/app/initialize_db.sql
```
### Créer un USER_A
Vous pouvez, remplacer les identifiants par les votres dans app/mysql_shortcut.py sans passer par cette étape.
Sinon :
```
mysql> SOURCE C:/Chemin/Vers/Mon/Dossier/app/create_user.sql
```
### Remplir la base de données
```
Chemin/Vers/Mon/Dossier/app>py fill_database.py
```
Cela devrais vous afficher :
```
Les données ont été remplacé par de nouvelles données
```
### Installer le requirements.txt
```
Chemin/Vers/Mon/Dossier>pip3 install -r requirements.txt
```
### Lancer l'application
```
Chemin/vers/mon/dossier>py main.py
```
