import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

# Parametri de generare
zile = 60
produse = ['Laptop', 'Telefon', 'Televizor', 'Casti', 'Monitor', 'Tastatura', 'Mouse', 'Tableta', 'Imprimanta', 'Camera Foto']

# Generare dataset
data = []
start_date = datetime(2024, 1, 1)
for zi in range(zile):
    numar_produse = random.randint(5, 15)  # Număr aleatoriu de produse per zi
    data_curenta = start_date + timedelta(days=zi)
    for _ in range(numar_produse):
        produs = random.choice(produse)
        pret = max(5, np.random.normal(40, 8))  # Preț: distribuție normală
        cantitate = random.randint(1, 10)  # Cantitate: distribuție uniformă
        promotie = random.random() < 0.3  # Probabilitate 30% de promoție
        if promotie:
            pret *= 0.8  # Reducere de 20%
        data.append([data_curenta, produs, cantitate, pret, promotie])

# Creare DataFrame
df_simulat = pd.DataFrame(data, columns=['Data', 'Produs', 'Cantitate', 'Pret', 'Promotie'])

# Calculul valorilor
df_simulat['Total_Vanzari'] = df_simulat['Cantitate'] * df_simulat['Pret']
df_simulat['Profit'] = df_simulat['Total_Vanzari'] * 0.3  # Marjă de profit 30%

# 1. Total vânzări per zi
vanzari_per_zi = df_simulat.groupby('Data')['Total_Vanzari'].sum().reset_index()
profit_per_zi = df_simulat.groupby('Data')['Profit'].sum().reset_index()

# 2. Statistici generale
statistici_generale = {
    "Media Preturilor": df_simulat['Pret'].mean(),
    "Pretul Max": df_simulat['Pret'].max(),
    "Pretul Min": df_simulat['Pret'].min(),
    "Media Cantitatilor": df_simulat['Cantitate'].mean(),
    "Cantitatea Max": df_simulat['Cantitate'].max(),
    "Cantitatea Min": df_simulat['Cantitate'].min(),
    "Profitul Total": df_simulat['Profit'].sum(),
    "Vanzarile Totale": df_simulat['Total_Vanzari'].sum()
}

# Afișare statistici
print("\nStatistici generale:")
for cheie, valoare in statistici_generale.items():
    print(f"{cheie}: {valoare:.2f}")
