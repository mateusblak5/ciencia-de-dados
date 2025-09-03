import pandas as pd
import numpy as np

# Criação de um dataset fictício
np.random.seed(42)

dados = pd.DataFrame({
    "Orcamento_Campanha": np.random.randint(1000, 5000, size=100),
    "Visualizacoes Anuncio": np.random.randint(2000, 20000, size=100),
    "Vendas": np.random.randint(10, 10000, size=100),
    "Cliques": np.random.randint(100, 20000, size=100)
})

# Visualizar a correlação entre cada variável
print(dados.corr().round(4))