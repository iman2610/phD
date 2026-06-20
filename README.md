# Air Quality Stability Prediction

Projet scientifique de machine learning visant à analyser et prédire la stabilité de la qualité de l’air à partir de données environnementales.

---

## Structure du projet

```
.
├── configs/
│   └── config.yaml
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── models/
│   ├── figures/
│   └── logs/
├── src/
│   ├── main.py
│   └── utils.py
├── requirements.txt
└── README.md
```

---

## Configuration

Toutes les configurations du projet sont centralisées dans :

```
configs/config.yaml
```

Exemples de paramètres :
- seed de reproductibilité
- chemins des données
- hyperparamètres du modèle
- paramètres de prétraitement

---

## Exécution du projet

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancer le pipeline principal
```bash
python -m src.main
```

---

## Fonctionnement du pipeline

1. Chargement de la configuration YAML  
2. Fixation de la graine aléatoire  
3. Chargement et prétraitement des données  
4. Entraînement du modèle ML  
5. Évaluation et génération des résultats  
6. Sauvegarde des modèles et figures  

---

## Matplotlib (mode serveur)

```python
matplotlib.use("Agg")
```

✔ Compatible serveur  
✔ Docker / CI/CD friendly  
✔ Pas d’interface graphique requise  

---

## Reproductibilité

- random seed Python
- NumPy seed
- Torch seed (optionnel)
- configuration YAML centralisée

---

## Dépendances principales

- numpy  
- pandas  
- matplotlib  
- pyyaml  
- scikit-learn  
- xgboost  

---

