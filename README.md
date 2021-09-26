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

:::danger
La requête doit absolument pointer sur le path du collecteur et la route generer par celui-ci doit être scrupuleusement respectée
**@app.route("/collector/info",methods=["POST"])**
:::

## Le collecteur global || router.py + dbconfig.py
