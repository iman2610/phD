import os
import random
import numpy as np
import yaml
from typing import Dict, Any


def load_config(config_path: str = "configs/config.yaml") -> Dict[str, Any]:
    """
    Charge un fichier de configuration YAML.

    Parameters
    ----------
    config_path : str
        Chemin vers le fichier config.yaml

    Returns
    -------
    dict
        Dictionnaire de configuration
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config


def set_seed(seed: int = 42):
    """
    Fixe les seeds pour assurer la reproductibilité.

    Parameters
    ----------
    seed : int
        Valeur de la graine aléatoire
    """
    random.seed(seed)
    np.random.seed(seed)

    # Pour reproductibilité plus stricte (si PyTorch est utilisé)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass