#Correlação e regressão
# Regressão linear para as variáveis X e Y da Tabela 5.1
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

d = {'Agente': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
     'Anos de serviço (X)': [2, 3, 4, 5, 4, 6, 7, 8, 8, 10],
     'Número de clientes (Y)': [48, 50, 56, 52, 43, 60, 62, 58, 64, 72]}
df = pd.DataFrame(data=d)

(a, b) = np.polyfit(x=df['Anos de serviço (X)'], y=df['Número de clientes (Y)'], deg = 1)

figure = plt.figure(figsize=(12, 8), facecolor='black')
plt.rcParams.update({"font.size": 22})
ax1 = figure.add_subplot(1, 1, 1)
ax1.plot(df['Anos de serviço (X)'], df['Número de clientes (Y)'], '.', markersize=15, color='yellow');
x = np.arange(df['Anos de serviço (X)'].min() - 1, df['Anos de serviço (X)'].max() + 2)
y = a*x + b
ax1.plot(x, y, linestyle='--', linewidth=3, color='deeppink');
ax1.set_facecolor('black')
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')
ax1.set_xlabel('Anos de serviço', color='white')
ax1.set_ylabel('Número de clientes', color='white')
ax1.spines['left'].set_color('white')
ax1.spines['right'].set_color('white')
ax1.spines['top'].set_color('white')
ax1.spines['bottom'].set_color('white')