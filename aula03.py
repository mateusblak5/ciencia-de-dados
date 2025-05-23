import matplotlib.pyplot as plt
import pandas as pd


def exibirGraficos():
    df = pd.DataFrame({
        "area": [125, 150, 142, 138, 160, 500, 485, 520, 478, 492, 1500, 90, 105, 112, 2000],
        "preco": [110, 130, 125, 120, 140, 400, 380, 420, 390, 405, 1000, 95, 105, 115, 1200]
    })

    plt.scatter(df['area'], df['preco'])
    plt.title('area (m²) x Preço (R$ mil)')

    plt.xlabel('area (m²)')
    plt.ylabel('Preço (R$ mil)')

    plt.grid(True)
    plt.show()

    plt.savefig('chart.png')

    # Removendo outliers usando IQR
    Q1 = df[["area", "preco"]].quantile(0.25)  # 1 quartil
    Q3 = df[["area", "preco"]].quantile(0.75)  # 3 quartil
    IQR = Q3 - Q1

    # filtra somente os dados mais próximos a mediana, exluindo os outliers
    mask = ~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
    df_limpo = df[mask]

    plt.scatter(df_limpo['area'], df_limpo['preco'])
    plt.title('area (m²) x Preço (R$ mil)')

    plt.xlabel('area (m²)')
    plt.ylabel('Preço (R$ mil)')

    plt.grid(True)
    plt.show()

    plt.savefig('chart2.png')