# Application de Visualisation de Données sur les Incendies de Forêt au Maroc

## Description

Ce projet consiste à créer une application de visualisation de données interactive utilisant les données marocaines pour prédire les incendies de forêt. L'application est construite avec Bokeh et permet aux utilisateurs d'interagir avec divers graphiques pour obtenir des informations approfondies sur le dataset.

## Dataset

Le dataset contient les colonnes suivantes :
- **Marqueurs temporels** : `acq_date`, `day_of_week`, `day_of_year` et les indicateurs liés aux jours fériés (`is_holiday`, `is_weekend`).
- **Caractéristiques spatiales** : `latitude`, `longitude` et `sea_distance`.
- **Conditions environnementales** : `NDVI` pour la santé de la végétation et `SoilMoisture`.
- **Données météorologiques** : `average_temperature`, `maximum_temperature`, `minimum_temperature`, `precipitation`, `snow_depth`, `wind_speed` et plus encore.
- **Statistiques météorologiques agrégées** : périodes hebdomadaires, mensuelles, trimestrielles et annuelles.
- **Variable de résultat** : `is_fire` indique la présence (1) ou l'absence (0) d'un incendie de forêt.

Ce dataset a été choisi en raison de sa nature complète, intégrant des données météorologiques, environnementales et spatiales pour faciliter la prédiction précise des incendies de forêt.

## Structure du Projet

Le projet est structuré comme suit :

- `main.py` : Contient le code de l'application Bokeh.
- `notebook.ipynb` : Un notebook Jupyter décrivant le dataset et les raisons de son choix, ainsi que le prétraitement des données.
- `README.md` : Ce fichier décrivant le projet.

## Prérequis

Pour exécuter ce projet, vous aurez besoin de :

- Python 3.x
- Les bibliothèques Python suivantes :
  - pandas
  - numpy
  - bokeh

## Installation

1. Clonez ce repository :
    ```bash
    git clone <votre-url-repository>
    ```
2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

Pour exécuter l'application Bokeh, utilisez la commande suivante :
```bash
bokeh serve --show main.py
```

Cela démarrera un serveur Bokeh et ouvrira l'application dans votre navigateur web par défaut.

## Contenu du Notebook

Le notebook Jupyter `notebook.ipynb` contient :

1. **Description du dataset** : Exploration initiale des données.
2. **Prétraitement des données** : Gestion des valeurs manquantes et normalisation des données.

## Auteurs

- LOUKILI Mehdi
- HABACH Abdelghafour
