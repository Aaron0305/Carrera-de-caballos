import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# Función para solicitar y validar los datos
def get_data():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            saldo = float(input("Ingrese el saldo en la cuenta de ahorros: "))
            transacciones = int(input("Ingrese el número de veces que usó la tarjeta de crédito: "))
            return saldo, transacciones
        except ValueError:
            print("Error: Por favor, ingrese valores numéricos válidos.")
            attempts += 1
    print("Se ha alcanzado el límite de intentos. El programa se ha detenido.")
    exit()

# Crear el DataFrame de clientes
saldo, transacciones = get_data()
clientes = pd.DataFrame({
    "saldo": [saldo],
    "transacciones": [transacciones]
})

# Escalar los datos
escalador = MinMaxScaler().fit(clientes.values)
clientes = pd.DataFrame(escalador.transform(clientes.values), columns=["saldo", "transacciones"])

# Realizar el clustering
kmeans = KMeans(n_clusters=7).fit(clientes.values)
clientes["cluster"] = kmeans.labels_

# Graficar los clusters
plt.figure(figsize=(6, 5), dpi=100)
colores = ["red", "blue", "orange", "black", "purple", "pink", "brown"]
for cluster in range(kmeans.n_clusters):
    plt.scatter(clientes[clientes["cluster"] == cluster]["saldo"],
                clientes[clientes["cluster"] == cluster]["transacciones"],
                marker="o", s=180, color=colores[cluster], alpha=0.5)
    plt.scatter(kmeans.cluster_centers_[cluster][0],
                kmeans.cluster_centers_[cluster][1],
                marker="P", s=280, color=colores[cluster])

plt.title("Clientes", fontsize=20)
plt.xlabel("Saldo en cuenta de ahorros (pesos)", fontsize=15)
plt.ylabel("Veces que usó tarjeta de crédito", fontsize=15)
plt.text(1.15, 0.2, "K = %i" % kmeans.n_clusters, fontsize=25)
plt.text(1.15, 0, "Inercia = %0.2f" % kmeans.inertia_, fontsize=25)
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.show()

del clientes["cluster"]

inercias = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k).fit(clientes.values)
    inercias.append(kmeans.inertia_)

plt.figure(figsize=(6, 5), dpi=100)
plt.scatter(range(2, 10), inercias, marker="o", s=180, color="purple")
plt.xlabel("Número de Clusters", fontsize=25)
plt.ylabel("Inercia", fontsize=25)
plt.show()