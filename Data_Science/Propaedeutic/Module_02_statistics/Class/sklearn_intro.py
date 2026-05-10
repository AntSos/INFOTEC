#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:22:12 2026

@author: irukandji
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

df_iris = pd.DataFrame(data = iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target

x = iris.data
y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)

predictions = model.predict(X_test)

precission = accuracy_score(Y_test, predictions)
print(f"Precission is {precission * 100:.2f}%")


"""
Example

"""

new_flower = pd.Series({
    'sepal length (cm)': 5.1,
    'sepal width (cm)': 3.5,
    'petal length (cm)': 1.4,
    'petal width': 0.2})

new_flower_array = new_flower.values.reshape(1, -1)



prediction = model.predict(new_flower_array)
specie = iris.target_names[prediction[0]]

print(f"The flower is: {specie}")
