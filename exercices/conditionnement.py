import numpy as np

# Matrice mal conditionnée (Hilbert modifiée)
A = np.array([
    [1.0, 1.0/2.0, 1.0/3.0],
    [1.0/2.0, 1.0/3.0, 1.0/4.0],
    [1.0/3.0, 1.0/4.0, 1.0/5.0]
])

b = np.array([1.0, 0.5, 0.3333])

# 1. Conditionnement
kappa_A = np.linalg.cond(A, 2)
print(f"Conditionnement kappa(A) = {kappa_A}")

# 2. Résolution exacte
x_exact = np.linalg.solve(A, b)

# 3. Perturbation du vecteur b
b_perturbe = b.copy()
b_perturbe[2] += 1e-14

# 4. Résolution perturbée
x_perturbe = np.linalg.solve(A, b_perturbe)

# 5. Erreur relative
erreur_relative = np.linalg.norm(x_exact - x_perturbe) / np.linalg.norm(x_exact)

print(f"Erreur relative : {erreur_relative:.6f}")