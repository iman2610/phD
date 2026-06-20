import numpy as np
import pandas as pd
import pytest

from src.preprocessing import split_and_scale


def test_split_reproducibility():
    """Vérifie l’invariance du partitionnement via la graine aléatoire."""

    # Génération d’un jeu de données de test fictif
    df = pd.DataFrame({
        'feature1': range(100),
        'feature2': range(100),
        'pm25': range(100)
    })

    config = {
        'data': {
            'target_column': 'pm25',
            'test_size': 0.2
        },
        'project': {
            'random_seed': 42
        },
        'preprocessing': {
            'scale_features': True
        }
    }

    # Deux appels successifs avec la même configuration
    X_train1, X_test1, y_train1, y_test1, _ = split_and_scale(df, config)
    X_train2, X_test2, y_train2, y_test2, _ = split_and_scale(df, config)

    # Vérification de l'identité des résultats
    np.testing.assert_array_equal(X_train1, X_train2)
    np.testing.assert_array_equal(X_test1, X_test2)
    np.testing.assert_array_equal(y_train1, y_train2)
    np.testing.assert_array_equal(y_test1, y_test2)