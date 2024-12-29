import numpy as np
import matplotlib.pyplot as plt

# Constantes
R = 1e-2  # m
I = 1  # A
M = 1e6  # kg
mu_0 = 4 * np.pi * 1e-7  # T m/A
V = (4/3) * np.pi * (1e-6)**3  # Volume

# Définition de la fonction F
def F(d):
    return (3 * mu_0 * I * V * M * R**2 * d) / (2 * (R**2 + d**2)**(5/2))

# Valeurs de d
d_values = np.linspace(0.015, 0.05, 100)  # distance mini egal au rayon de la pipette et distance maxi fixé à 0.1m

# Calcul de F pour les valeurs de d
F_values = F(d_values)

# Tracer F en fonction de d
plt.plot(d_values, F_values)
plt.title("Fonction $F(d)$ en fonction de $d$")
plt.xlabel("$d$ (m)")
plt.ylabel("$F(d)$ (N)")
plt.grid()
plt.ylim(bottom=0)  # Pour éviter les valeurs négatives
plt.show()