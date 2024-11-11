<!-- INTRODUCTION -->
<br />
<div align="center">
  <img src="https://github.com/Leeexyy4/Guilbert_Emma_LabyrintheDijkstra_Python/blob/main/plan_supermarche.png" alt="Logo" width="*" height="*">

  <p align="center">
    Projet réalisé en 1ère année de BUT Informatique - 2022     
    .
    <a src="url source">View Demo</a>
  </p>
  

  <img src="https://contrib.rocks/image?repo=Leeexyy4/Guilbert_Emma_LabyrintheDijkstra_Python" />
  
  </br>
  Statut du projet : Terminé
  </br>
  </br>
</div>



<!-- TABLE DES MATIERES -->
<details>
  <summary>Table des matières</summary>
  <ol>
    <li><strong>Description</strong>
      <ul>
        <li><a href="#description-du-jeu">Description du jeu</a></li>
        <li><a href="#description-du-projet">Description du projet</a></li>
      </ul>
    </li>
    <li><strong>Installation</strong>
      <ul>
        <li><a href="#techniques-utilisées">Techniques utilisées</a></li>
        <li><a href="#pré-requis-à-linstallation">Pré-requis à l'installation</a></li>
        <li><a href="#installation">Installation du projet</a></li>
      </ul>
    </li>
    <li><strong>En savoir plus</strong>
      <ul>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#sources">Sources</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- Description du projet -->
### Description du projet
<!-- Le scénario -->
**Labyrinthe Dijkstra** est un jeu dans lequel le but est de se déplacer à travers un labyrinthe en utilisant l'algorithme de Dijkstra pour trouver le chemin le plus court entre deux points spécifiques. 

<!-- L'objectif -->
L'objectif du jeu est de réussir à réaliser le chemin le plus court dans le super-marché en fonction des aliments d'une liste de course prédéfinie.

Explication de l'algorithme "algo_plus_court" par étapesInitialisation du départ et du chemin : L'algorithme commence par définir une position de départ et initialise une liste représentant le chemin, qui commence avec la case de départ.

Calcul des chemins pour chaque produit : Tant que la liste des produits à atteindre n'est pas vide, l'algorithme cherche le chemin le plus court vers chaque produit, met à jour la distance minimale et ajoute ce chemin au chemin final.

Mise à jour de la distance totale : À chaque fois qu'un produit est atteint, la distance parcourue est ajoutée à la distance totale.

Recherche de la caisse la plus proche : L'algorithme évalue la distance vers chaque caisse, met à jour la caisse la plus proche et ajoute le chemin correspondant au chemin final.

Calcul du chemin jusqu'à la sortie et renvoi du résultat : L'algorithme poursuit le calcul du chemin jusqu'à la sortie et renvoie le chemin complet, incluant tous les produits et la caisse la plus proche.

Une fois que tout le parcours est terminé, l'algorithme renvoie le chemin complet du départ à la sortie.

<p align="right"><a href="#readme-top">&#8593</a></p>

### Techniques utilisées

Le projet a été réalisé en utilisant le langage **Python** et la bibliothèque **Pygame** pour l'interface graphique et la gestion du labyrinthe. L'algorithme de Dijkstra a été implémenté pour résoudre le problème du chemin le plus court.

<p align="right"><a href="#readme-top">&#8593</a></p>

### Pré-requis à l'installation

- Python version 3.12.1
- Dépendances Pygame

<p align="right"><a href="#readme-top">&#8593</a></p>

### Installation

Afin de télécharger et d'installer le jeu, veuillez à avoir une version de python à la version 3.12.1

1. Clone le repertoire
   ```sh
   git clone https://github.com/Leeexyy4/Guilbert_Emma_LabyrintheDijkstra_Python.git
   ```
2. Installer la dépendance pygame
   ```sh
   pip install pygame
   ```

<p align="right"><a href="#readme-top">&#8593</a></p>


<!-- CONTACT -->
## Contact

[Linkedin](https://www.linkedin.com/in/emma-guilbert-29567b265/)

[Github](https://github.com/Leeexyy4/Guilbert_Emma_LabyrintheDijkstra_Python) 

[Mail](emmaguilbert4@gmail.com)

<p align="right"><a href="#readme-top">&#8593</a></p>


<!-- SOURCES -->
## Sources

<a href="https://www.python.org/downloads/">
    <img src="https://simpleicons.org/icons/python.svg" alt="Python" style="width:30px; height:30px;">
</a>


<p align="right"><a href="#readme-top">&#8593</a></p>
