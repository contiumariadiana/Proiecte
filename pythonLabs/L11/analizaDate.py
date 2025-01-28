import pandas as pd

# Încarcă fișierul CSV într-un DataFrame
df = pd.read_csv("vanzari.csv")

# Convertirea coloanei 'Data' în format datetime
df['Data'] = pd.to_datetime(df['Data'], format='%m/%d/%Y')

# 1. Cele mai vândute produse pe lună
df['Luna'] = df['Data'].dt.to_period('M')  # Extrage luna și anul
cele_mai_vandute = df.groupby(['Luna', 'Produs'])['Cantitate'].sum().reset_index()
cele_mai_vandute = cele_mai_vandute.loc[cele_mai_vandute.groupby('Luna')['Cantitate'].idxmax()]
print("Cele mai vândute produse pe lună:")
print(cele_mai_vandute)

# 2. Venitul total pe fiecare produs
df['Venit'] = df['Cantitate'] * df['Pret']
venit_total_pe_produs = df.groupby('Produs')['Venit'].sum().reset_index()
print("\nVenitul total pe fiecare produs:")
print(venit_total_pe_produs)

# 3. Filtrarea vânzărilor într-un interval de timp specific
start_date = "2024-01-01"
end_date = "2024-03-31"
vanzari_filtrate = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]
print(f"\nVânzările între {start_date} și {end_date}:")
print(vanzari_filtrate)

# 4. Venitul mediu lunar
venitul_mediu_lunar = df.groupby('Luna')['Venit'].mean().reset_index()
print("\nVenitul mediu lunar:")
print(venitul_mediu_lunar)
