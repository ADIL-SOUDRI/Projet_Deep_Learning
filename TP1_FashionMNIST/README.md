#  FashionMNIST Classification - Projet Deep Learning

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)



---

##  Description du projet

Ce projet implémente un réseau de neurones convolutif (CNN) pour la classification d'images du dataset **FashionMNIST**. L'objectif est de reconnaître 10 catégories d'articles vestimentaires à partir d'images en niveaux de gris de taille 28×28 pixels.

###  Dataset FashionMNIST

| Caractéristique | Valeur |
|----------------|--------|
| Images d'entraînement | 60,000 |
| Images de test | 10,000 |
| Résolution | 28×28 pixels |
| Canaux | 1 (niveaux de gris) |
| Classes | 10 catégories |

**Les 10 classes :**
- 👕 T-shirt/top
- 👖 Trouser
- 🧥 Pullover
- 👗 Dress
- 🧥 Coat
- 👡 Sandal
- 👕 Shirt
- 👟 Sneaker
- 👜 Bag
- 👢 Ankle boot

---

##  Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python** 3.9 ou supérieur
- **Anaconda** (recommandé) ou Miniconda
- Au moins **8 Go** de RAM (recommandé)
- **GPU** (optionnel, mais recommandé pour l'entraînement rapide)

---

##  Installation
pip install torch torchvision torchaudio numpy pandas matplotlib scikit-learn seaborn tqdm
