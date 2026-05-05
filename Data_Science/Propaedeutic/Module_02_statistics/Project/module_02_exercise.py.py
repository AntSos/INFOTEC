#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:12:21 2026

@author: irukandji
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

print('*' * 127)
print("""1. Cargar el archivo CSV synthetic_customer_data.csv en un DataFrame usando Pandas y mostrar las primeras filas
 para comprender la estructura de los datos.
""")
# File load.
file_name = 'synthetic_customer_data.csv'
file_path = f'/home/irukandji/Documents/INFOTEC/Data_Science/Propaedeutic/Module_02_statistics/Project/{file_name}'
# Pandas csv df.
customer_data = pd.read_csv(file_path)
# Show first 15 th rows.
print(customer_data.head(15))
print('*' * 127)
print("""
2. Mostrar información básica del DataFrame, como el tipo de datos de cada columna 
y calcular estadísticas descriptivas para cada variable.
""")
# Data general info for each column, including data type.
print(customer_data.info())
print('*' * 127)
# Data descriptive statistics.
print(customer_data.describe())
print('*' * 127)
print("""
3. Visualización de Datos:

    - Generar histogramas para analizar la distribución de age y total_spent.
    - Crear un gráfico de barras para observar la distribución de gender.
""")
# Seaborn barplot age vs total_spent
sns.barplot(x='age', y='total_spent', data=customer_data, hue='age')
plt.title('Age vs total spent distribution')
plt.show()
# Gender distribution.
sns.countplot(x='gender', data=customer_data, hue='gender')
plt.title('Gender distribution')
plt.show()
print('*' * 127)
print("""
      4. Preprocesamiento de los Datos:

          - Verificar si existen valores nulos en el conjunto de datos y documentar los resultados.
          - Codificar la variable gender en valores numéricos (0 para Female, 1 para Male).
          - Escalar las columnas numéricas (age, total_spent, frequency, days_since_last_purchase) usando StandardScaler para asegurar consistencia en las escalas.
""")
# Check null values for each column.
print(customer_data.isnull())
# Create a deep copy of customer_data to avoid changes in the original data.
dc_customer_data = customer_data.copy(deep=True)
# Change gender codification: 0 for Female and 1 for Male, using map method.
dc_customer_data ['gender'] = dc_customer_data ['gender'].map({'Male' : 1, 'Female' : 0}, na_action=None).astype(int)
# Print dc_customer_data gender column.
print(dc_customer_data['gender'])
# Check dc customer_data general info for each column (gender now is 100 int64 values without null).
print(dc_customer_data.info())
# Instance StandardScaler object.
scaler = StandardScaler()
# Select the desired columns to scale from dc_customer_data.
scale_colums = ['age', 'total_spent', 'frequency', 'days_since_last_purchase']
# Check columns before scale.
print(dc_customer_data[['age', 'total_spent', 'frequency', 'days_since_last_purchase']])
# Apply fit_transform method to the selected columns.
dc_customer_data[scale_colums] = scaler.fit_transform(dc_customer_data[scale_colums])
# Check columns after scale.
print(dc_customer_data[['age', 'total_spent', 'frequency', 'days_since_last_purchase']])
