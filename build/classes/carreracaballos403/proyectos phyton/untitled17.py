# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:13:06 2024
@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs, make_circles
import matplotlib
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

# Generamos 30 muestras con dos características, asociadas a dos clases
X, y = make_blobs(n_samples=30, n_features=2, centers=2, random_state=21, center_box=(0, 10.0))

# Creamos el modelo SVM para clasificación con kernel lineal y entrenamos el modelo
clf = svm.SVC(kernel='linear', C=100)
clf.fit(X, y)

# Graficamos los datos en el espacio de características
cmap = matplotlib.colors.ListedColormap(['k', 'g'])
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=cmap)

# Creamos un mesh para evaluar la función de decisión
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# Graficamos el hiperplano y el margen
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# Graficamos los vectores soporte
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k')

Z_pred = clf.predict(np.c_[XX.ravel(), YY.ravel()])
Z_pred = Z_pred.reshape(XX.shape)

cmap = matplotlib.colors.ListedColormap(['r', 'y'])
plt.pcolormesh(XX, YY, Z_pred, cmap=cmap, alpha=0.1)

new_x = [[5, 0.5]]
new_z = clf.predict(new_x)
color = 'k' if new_z[0] == 0 else 'g'
plt.scatter(new_x[0][0], new_x[0][1], marker='+', color=color, s=300)
plt.grid()
plt.show()

# Veamos el uso de kernels para el problema de clases linealmente no separables

# Generamos 100 muestras con dos características, asociadas a dos clases
X, y = make_circles(100, factor=.2, noise=.2)

# Creamos el modelo SVM para clasificación con kernel lineal/rbf y entrenamos el modelo
clf = svm.SVC(kernel='linear', C=100).fit(X, y)

# Graficamos los datos en el espacio de características
cmap = matplotlib.colors.ListedColormap(['k', 'g'])
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=cmap)

# Creamos un mesh para evaluar la función de decisión
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# Graficamos el hiperplano y el margen
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# Graficamos los vectores soporte
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k')

Z_pred = clf.predict(np.c_[XX.ravel(), YY.ravel()])
Z_pred = Z_pred.reshape(XX.shape)

cmap = matplotlib.colors.ListedColormap(['r', 'y'])
plt.pcolormesh(XX, YY, Z_pred, cmap=cmap, alpha=0.1)

plt.grid()
plt.show()

# Veamos el efecto del truco kernel (aumentando la dimensionalidad del espacio de entradas)
from mpl_toolkits import mplot3d

# Aplicamos una operación de kernel gaussiano para separar las clases
# Gamma controla el efecto del kernel, si es muy pequeño el modelo se parece al lineal
gamma = 1
Xr = np.exp(-gamma * (X ** 2).sum(1))

# Graficamos el espacio de características mapeado por el kernel
ax = plt.subplot(projection='3d')
cmap = matplotlib.colors.ListedColormap(['k', 'g'])
ax.scatter3D(X[:, 0], X[:, 1], Xr, c=y, s=50, cmap=cmap)

# Cargamos el dataset
digits = load_digits()
digits.data.shape

# Mostramos los dígitos en imágenes
fig = plt.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

for i in range(10):
    ax = fig.add_subplot(2, 5, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]))

# Definimos la configuración del clasificador

Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target, random_state=0)

clf = svm.SVC(kernel='linear')

# Entrenamos el clasificador con los datos de entrenamiento
clf.fit(Xtrain, ytrain)

score = clf.score(Xtest, ytest)
print(score)

ypred = clf.predict(Xtest)
matriz = confusion_matrix(ytest, ypred)

plot_confusion_matrix(conf_mat=matriz, figsize=(6, 6), show_normed=False)
plt.tight_layout()
plt.show()
