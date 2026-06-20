"""
Module de pretraitement des donnees
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from typing import Tuple, Dict, Any

def clean_data(df: pd.DataFrame, config: Dict[str, Any]) -> pd.DataFrame:
    df_clean = df.copy()

    handle_missing = config['preprocessing']['handle_missing']

    # 1. Gestion des valeurs manquantes
    for col in df_clean.columns:
        if df_clean[col].isnull().any():

            if handle_missing == 'median':
                # Calcul de la médiane et imputation
                median_value = df_clean[col].median()
                df_clean[col] = df_clean[col].fillna(median_value)

    # 2. Gestion des valeurs aberrantes (Outliers via IQR)
    threshold = config['preprocessing']['outlier_threshold']
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        if col != config['data']['target_column']:

            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1

            # Bornes IQR
            lower = Q1 - threshold * IQR
            upper = Q3 + threshold * IQR

            # Neutralisation des outliers
            df_clean[col] = df_clean[col].clip(lower, upper)

    return df_clean