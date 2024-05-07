import pandas as pd
import matplotlib.pyplot as plt

data = {'nome': ['javid', 'alenri', 'samuel', 'aloizio', 'angel'],
        'idade': [25, 30, 35, 45, 35],
        'departamento': ['policia', 'advogado', 'medico', 'bombeiro', 'segurança'],
        'salario': [2500, 3000, 2000, 2800, 3500]}
df = pd.DataFrame(data)
nome_coluna = df['nome']
print(nome_coluna)

colunas_especificas = df[['nome', 'salario']]
print(colunas_especificas)

df['Salario_Anual'] = df['salario'] * 12
print(df)

df = pd.DataFrame(data)


plt.plot (df['idade'],(df['salario']))
plt.title('tendencias ao longo do tempo')
plt.xlabel('idade')
plt.ylabel('salario')
plt.show()

