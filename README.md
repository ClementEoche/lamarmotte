# Documentation technique Au Bon Beurre

## Introduction

Pour la société Au Bon Beurre, la société 100% bretonne beurre salé only, nous proposons un outil web permettant de monitorer les unitées de productions avec une fiabilité maximale sur les infos des differentes sondes. Pour assuré la meilleur image de la société aupres de ses consommateurs nous nous assurerons également d'une sécurité accrue sur la solution proposé.

### :hammer_and_wrench: Nos outils de developpement de la solution

* Python pour le traitement des données
* HTML CSS JS + librairie chartJS pour l'IHM
* MariaDB pour le stockage des données
* NGinx pour le server contenant l'ensemble du service web
* Docker pour creer et deployer nos solutions couplé avec GitHub

:::success
Les données echangées entre les interfaces de BDD et les éléments exterieurs s'effecturons avec le format de données JSON
:::

## Schématisation de notre solution
![](https://i.imgur.com/20jA9cf.png)

Le schémas ci-dessus modélise la solution initial sur les echange d'informations entre les unité de production et le traitement qui s'en suis dans l'outil pour arrivé à un affichage des informations élémentaire au bon deroulement des productions de la société Au Bon Beurre.

:::warning
La solution actuelle ne comporte pas tout les éléments de sécurisation du code dans l'attente du responsable de projet pour initialiser la production des éléments de sécurité.
:::
## Simulation de relever de capteurs || randomvalues.py
Pour simuler les capteurs des unités de productions et dans un objectif de tester le bon fonctionnement du système, nous avons mis au point un script python de generation de valeurs aleatoires. Les valeurs sont generées lorsque les sockets appellent ce script. 

## Unitées de productions || socket.py

Lorsque les sockets python recuperent les informations générées "par les sondes" (cf. Simulation de relever de capteurs), ils effectueront un envoi sur un collecteur global sous format JSON. 

Cette envoie contiendra dans le body les attributs suivant dans une requete POST. 
```json
                "unityId" : unityid,
		"tmp_Cuve" : tmp_Cuve,
		"tmp_Ext" : tmp_Ext,
		"poids_Lait_Cuve" : poids_Lait_Cuve,
		"mesure_PH" : mesure_PH,
		"mesure_K" : mesure_K,
		"concentration_NaCl" : concentration_NaCl,
		"niv_Bact_Salmonelle" : niv_Bact_Salmonelle,
		"niv_Bact_Ecoli" : niv_Bact_Ecoli,
		"niv_Bact_Listeria" : niv_Bact_Listeria
```
        

:::danger
La requête doit absolument pointer sur le path du collecteur et la route generer par celui-ci doit être scrupuleusement respectée
**@app.route("/collector/info",methods=["POST"])**
:::

## Le collecteur global || router.py + dbconfig.py

Le collecteur est l'équivalent d'une API mais n'a pour seul objectif que d'inserer les valeurs relevées par les unités de productions. 
Le collecteur va donc ouvrir une route accessible au unité de production pour effectuer une requete POST avec un body chargé avec les informations des unités.
:::info
**Le collecteur est accessible via : exemplehttp://localhost/nomdeprojet/collectors/collectorunity/(route generé par le script py)**
:::
Le collecteur est configuré sur la base MariaDB avec des informations sensibles de connexions pour effectuer les actions necessaires pour modifier la base de données (INSERT).

Une fois l'ensemble de ces parametres réunis le collecteur chargera en base l'ensemble des informations qu'il aura reçu.

## La base de données MariaDB

La base permet de stocker l'ensembles des données recuperer par le collecteur. Ci-dessous la structure type d'une table de la base de données pour le stockage de l'informations des unités de productions.

Chaque jeux de données sera identifié par un id unique ainsi que l'id de l'unité de production. 
```sql
CREATE TABLE IF NOT EXISTS unities
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    unityId INT,
    tmp_Cuve FLOAT,
    tmp_Ext FLOAT,
    poids_Lait_Cuve FLOAT,
    mesure_PH FLOAT,
    mesure_K FLOAT,
    concentration_NaCl FLOAT,
    niv_Bact_Salmonelle FLOAT,
    niv_Bact_Ecoli FLOAT,
    niv_Bact_Listeria FLOAT,
    date_info DATE
);
```

## Collecteur Writable & Readable

Les collecteurs Writable et Readable à l'instar du collecteur global n'ont pas pour fonctions de relier les informations des unités de production à la BDD. 

Ils seront egalement construit avec le langage python.

Ils vont servir comme service d'interface de base de données pour echanger les informations stocker en base à une IHM (ou application web).
:::info
**Le but finalement étant tout simplement de relier l'interface utilisateur à la base de données de manière decentralisées.** A la fois pour des raisons de securité (ne pas stocker des informations de connexion de db sur l'interface utilisateur) et pour des raisons de scalabilité (si le systeme venait à acceuillir de nouvelles données le code est plus facilement comprehensible et adaptable)
:::

## Interface Utilisateur

L'interface utilisateur va permettre via le fetching de nos collecteurs (writable et readable) d'afficher les informations contenu en base et de creer une IHM clair et compréhensible pour les techniciens qui doivent analysé les relever des sondes. 

Pour cela notre interface ou plutot application web, va être construite à l'aide de **ChartJS, JS, HTML & CSS**.

:::success
**Le fetching précedement cité correspont tout simplement à la methode de recuperation d'information traité par javascript**
La methode de fetch va récuperer des informations via une requete sur une API ou dans notre situation sur nos collecteurs de type GET
On peut egalement envoyer des informations avec une requete de type POST
:::