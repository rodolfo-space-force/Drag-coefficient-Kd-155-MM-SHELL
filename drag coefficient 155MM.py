#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Curva K_D(M) – ajuste por trechos (original 155 mm)
# ------------------------------------------------------------
def KD_of_M(M):
    M = float(M)
    if M < 0.5:
        M = 0.5
    if M > 2.6:
        M = 2.6

    if M <= 0.90:
        return 0.0579080038

    if 0.90 < M <= 0.96:
        x = M
        return (44.26302428
                - 138.8317032*x
                + 144.7922431*x**2
                - 50.12112525*x**3)

    if 0.96 < M <= 1.02:
        x = M
        return (414.3525910
                - 1262.4596067*x
                + 1280.9650680*x**2
                - 432.7252631*x**3)

    if 1.02 < M <= 1.22:
        x = M
        return (-0.4212674799
                + 1.029831902*x
                - 0.4621525076*x**2)

    if 1.22 < M <= 1.30:
        x = M
        return (8.911875950
                - 20.35167306*x
                + 15.77773047*x**2
                - 4.085776562*x**3)

    # 1.30 < M <= 2.60
    x = M
    return ((0.9415 + 0.1327*x)**2 - 1.0) / (x**2)


# ------------------------------------------------------------
# Amostragem e plot
# ------------------------------------------------------------
Mach = np.linspace(0.5, 2.6, 2000)
KD = np.array([KD_of_M(M) for M in Mach])

plt.figure(figsize=(7, 4))
plt.plot(Mach, KD)
plt.xlabel("Mach")
plt.ylabel("K_D")
plt.title("Coeficiente de arrasto balístico K_D × Mach (155 mm)")
plt.grid(True)
plt.show()

# Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.



