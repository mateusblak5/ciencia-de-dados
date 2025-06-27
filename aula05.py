import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Conjunto de dados exemplo
dados = [10, 20, 20, 30, 40, 50, 50, 50, 60, 70, 80, 90, 100]

# Calcular quartis
quartis = np.percentile(dados, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')