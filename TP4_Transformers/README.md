#  TP4 – Transformers NLP Project

##  Description

Ce projet a pour objectif d’étudier et d’implémenter les modèles **Transformers** appliqués au **Traitement Automatique du Langage Naturel (NLP)**.

Il permet de comprendre les modèles modernes tels que **BERT, DistilBERT, T5 et XLM-R**, ainsi que leurs applications dans différentes tâches NLP :

- Classification de texte  
- Génération de texte  
- Résumé automatique  
- Question Answering  
- Analyse multilingue  
- Fine-tuning de modèles  
- Compression de modèles  
- Implémentation d’un mini-Transformer from scratch  

---

##  Objectifs du projet

- Comprendre l’architecture Transformer et le mécanisme d’attention  
- Utiliser des modèles pré-entraînés via Hugging Face  
- Expérimenter plusieurs tâches NLP modernes  
- Comparer les performances de différents modèles  
- Visualiser les résultats (loss, accuracy, attention maps)  
- Implémenter un mini Transformer from scratch  

---

##  Structure du projet

TP4_Transformers/

├── data/
│   └── simple_textes.txt
│
├── notebooks/
│   ├── 01_introduction.ipynb
│   ├── 02_classification.ipynb
│   ├── 03_transformer_anatomy.ipynb
│   ├── 04_multilingual_processing.ipynb
│   ├── 05_text_generation.ipynb
│   ├── 06_summarization.ipynb
│   ├── 07_question_answering.ipynb
│   ├── 08_fine_tuning_advanced.ipynb
│   ├── 09_model_compression.ipynb
│   ├── 10_few_to_no_labels.ipynb
│   ├── 11_transformers_from_scratch.ipynb
│   └── 12_future_directions.ipynb
│
├── images/
│   ├── attention_maps/
│   │   ├── attention_map.png
│   │   └── attention_widget.png
│   │
│   └── training_curves/
│       ├── accuracy_curve.png
│       └── loss_curve.png
│
├── environment.yml
├── requirements.txt
├── setup.py
└── README.md

---

##  Installation

### 1. Cloner le projet
```bash
git clone <repo-url>
cd TP4_Transformers

##  Créer l’environnement
conda env create -f environment.yml
conda activate tp4_env
3. Installer les dépendances
pip install -r requirements.txt
