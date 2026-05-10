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
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score,f1_score, roc_auc_score, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


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
print('*' * 127)
print(""" 
5. Dividir los Datos en Entrenamiento y Prueba:

   - Definir las características (X) y la variable objetivo (y), que es returned_next_month.
   - Dividir los datos en un conjunto de entrenamiento y otro de prueba (80/20).
""")
# Define X and y.
# Explanatory variables, drop customer_id and returned_next_month.  
X = dc_customer_data.drop(columns=['customer_id', 'returned_next_month'])
# Response, keep only returned next month.
y = dc_customer_data['returned_next_month']
# Divide training and testing 80/20.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Check accuracy score.
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
pressicion = accuracy_score(y_test, predictions)
print(f"Model train/test pressicion is: {pressicion * 100}%")
print('*' * 127)
print("""
6. Entrenamiento de Modelos:

    - Seleccionar tres modelos de clasificación: Regresión Logística, Árbol de Decisión y Bosque Aleatorio.
    - Entrenar cada modelo usando los datos de entrenamiento.
""")
      
# Logistic regression model instance.
lg_model = LogisticRegression(max_iter=1000)
# Train model.
lg_model.fit(X_train, y_train)
# Predictions.
y_prediction = lg_model.predict(X_test)
# Evaluate the model.
print(f"Logistic Regression Accuracy = {accuracy_score(y_test, y_prediction) * 100}%", end='\n\n')
print("Logistic regression confusion matrix is:", end='\n\n')
print(confusion_matrix(y_test, y_prediction))
print("Logistic regression clasification report:", end='\n\n')
print(classification_report(y_test, y_prediction))

# Tree model instance.
t_model = DecisionTreeClassifier(random_state=42, max_depth=5)
# Train model.
t_model.fit(X_train, y_train)
# Predictions.
y_t_prediction = t_model.predict(X_test)
# Evaluate the model.
print(f"Decission tree accuracy = {accuracy_score(y_test, y_t_prediction) * 100}%", end='\n\n')
print("Decission tree confusion matrix is:", end='\n\n')
print(confusion_matrix(y_test, y_t_prediction))
print("Decission tree  clasification report:", end='\n\n')
print(classification_report(y_test, y_t_prediction))
# Plot the tree.
plt.figure(figsize=(15, 8))
tree.plot_tree(t_model, feature_names=X.columns, class_names=['0', '1'], filled=True)
plt.show()

# Random forest instance.
rf_model = RandomForestClassifier(n_estimators=200, random_state=42, max_depth=10, min_samples_split=5)
# Train model.
rf_model.fit(X_train, y_train)
# Predictions.
y_rf_prediction = rf_model.predict(X_test)
# Evaluate the model.
print(f"Random forest accuracy = {accuracy_score(y_test, y_rf_prediction) * 100}%", end='\n\n')
print("Random forest confusion matrix is:", end='\n\n')
print(confusion_matrix(y_test, y_rf_prediction))
print("Random forest  clasification report:", end='\n\n')
print(classification_report(y_test, y_rf_prediction))
print('*' * 127)
print("""
7. Evaluación Inicial de Modelos:

    - Evaluar cada modelo en el conjunto de prueba usando métricas de rendimiento: exactitud, precisión, recall, F1 y AUC-ROC.
    - Comparar los resultados y documentarlos para seleccionar el mejor modelo.
""")
      
# Logistic regression metrics.
lg_accuracy = accuracy_score(y_test, y_prediction)
lg_precision = precision_score(y_test, y_prediction)
lg_recall = recall_score(y_test, y_prediction)
lg_f1 = f1_score(y_test, y_prediction)
# Probabilities.
y_probability = model.predict_proba(X_test)[:, 1]
lg_auc = roc_auc_score(y_test, y_probability)
# Decission tree metrics.
t_accuracy = accuracy_score(y_test, y_t_prediction)
t_precision = precision_score(y_test, y_t_prediction)
t_recall = recall_score(y_test, y_t_prediction)
t_f1 = f1_score(y_test, y_t_prediction)
# Probabilities.
t_probability = model.predict_proba(X_test)[:, 1]
t_auc = roc_auc_score(y_test, t_probability)
# Random forest metrics.
rf_accuracy = accuracy_score(y_test, y_rf_prediction)
rf_precision = precision_score(y_test, y_rf_prediction)
rf_recall = recall_score(y_test, y_rf_prediction)
rf_f1 = f1_score(y_test, y_rf_prediction)
# Probabilities.
rf_probability = model.predict_proba(X_test)[:, 1]
rf_auc = roc_auc_score(y_test, rf_probability)
# Print values.
print(f"Logistic regression: Accuracy = {lg_accuracy}, Precision = {lg_precision}, Reecall = {lg_recall}, F1 = {lg_f1}, AUC-ROC = {lg_auc}")
print(f"Decision Tree: Accuracy = {t_accuracy}, Precision = {t_precision}, Reecall = {t_recall}, F1 = {t_f1}, AUC-ROC = {t_auc}")
print(f"Random forest: Accuracy = {rf_accuracy}, Precision = {rf_precision}, Reecall = {rf_recall}, F1 = {rf_f1}, AUC-ROC = {rf_auc}")
print("""
      Los tres modelos presentan los mismos valores de: rendimiento: exactitud, precisión, recall, F1 y AUC-ROC.
      Por lo que cualquiera de ellos puede ser utilizado.
""")
print('*' * 127)    
print("""
8. Optimización del Mejor Modelo:

    - Realizar optimización de hiperparámetros (Grid Search) en el modelo seleccionado (en este caso, Bosque Aleatorio).
    - Ajustar el modelo con los mejores parámetros encontrados y entrenarlo nuevamente.
      
""")
# Grid parameters.
param_grid = {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 3],
                'bootstrap': [True, False]
              }
# Grid search instance.
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=1, verbose=0)
# Training.
grid_search.fit(X_train, y_train)
print(f"Best parameters -> {grid_search.best_params_}")
print(f"Best accuracy -> {grid_search.best_score_}")
print('*' * 127) 
print("""
9. Validación y Análisis de Errores:

   - Evaluar el rendimiento del modelo optimizado en el conjunto de prueba con las métricas mencionadas.
   - Generar la matriz de confusión para identificar y analizar los errores de clasificación.
""")

# Best model.
best_model = grid_search.best_estimator_
rf_y_prediction = best_model.predict(X_test)
# Random forest metrics.
rf_accuracy = accuracy_score(y_test, rf_y_prediction)
rf_precision = precision_score(y_test, rf_y_prediction)
rf_recall = recall_score(y_test, rf_y_prediction)
rf_f1 = f1_score(y_test, rf_y_prediction)
# Probabilities.
rf_probability = model.predict_proba(X_test)[:, 1]
rf_auc = roc_auc_score(y_test, rf_probability)
# Confusion matrix.
ConfusionMatrixDisplay.from_estimator(best_model, X_test, y_test)
print(f"Random forest: Accuracy = {rf_accuracy}, Precision = {rf_precision}, Reecall = {rf_recall}, F1 = {rf_f1}, AUC-ROC = {rf_auc}")
print("Cofusion matrix: ")
plt.show
print('*' * 127) 
print("""
10. Conclusión y Recomendaciones:
          
   Con los valores presentados por el modelo random forest, es posible estimar la retencion de clientes; sin embargo,
   debido al tamano del conjunto de datos, existe la posibilidad de requerir un reajuste o validacion cruzada, asi como,
   incluir mas datos y tecnicas adicionales antes de generalizar y emplear el modelo de forma cotidiana.
""")