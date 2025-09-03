import pandas as pd
import matplotlib.pyplot as plt

def calcular_quartis_e_plotar():
    # Criando um DataFrame pandas com dados de exemplo
    dados = {
        'Notas': [10, 20, 20, 30, 40, 50, 50, 50, 60, 70, 80, 90, 100]
    }
    df = pd.DataFrame(dados)
    
    # Calculando quartis usando pandas
    quartis = df['Notas'].quantile([0.25, 0.5, 0.75])
    q1 = quartis[0.25]
    q2 = quartis[0.5]
    q3 = quartis[0.75]
    
    # Imprimindo os resultados
    print(f'Quartis calculados:')
    print(f'Q1 (25%): {q1}')
    print(f'Q2 (Mediana - 50%): {q2}')
    print(f'Q3 (75%): {q3}')
    
    # Criando o boxplot
    plt.figure(figsize=(10, 6))
    df.boxplot(column='Notas', vert=False, grid=False)
    
    # Adicionando título e rótulos
    plt.title('Distribuição de Notas - Boxplot', pad=20, fontsize=16)
    plt.xlabel('Valores das Notas', fontsize=12)
    
    # Personalizando a aparência
    plt.axvline(x=q1, color='red', linestyle='--', alpha=0.5, label=f'Q1: {q1}')
    plt.axvline(x=q2, color='green', linestyle='--', alpha=0.5, label=f'Q2: {q2}')
    plt.axvline(x=q3, color='blue', linestyle='--', alpha=0.5, label=f'Q3: {q3}')
    plt.legend()
    
    # Salvando a figura
    plt.savefig('boxplot_notas.png', dpi=300, bbox_inches='tight')
    print("\nBoxplot salvo como 'boxplot_notas.png'")
    
    # Mostrando o gráfico
    plt.show()

if __name__ == "__main__":
    calcular_quartis_e_plotar()