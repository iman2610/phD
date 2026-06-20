import sys
import os
import matplotlib

# Bascule de Matplotlib sur un backend non-interactif
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from src.utils import load_config, set_seed


def main():
    # Chargement du fichier de configuration YAML
    config = load_config("configs/config.yaml")

    # Fixation universelle des graines pour la reproductibilité
    set_seed(config['project']['random_seed'])

    print("[RUN] Execution du pipeline scientifique...")

    # Le reste du code exécute les étapes de prétraitement
    # et d'apprentissage ...


if __name__ == "__main__":
    main()