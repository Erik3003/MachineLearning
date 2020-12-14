import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


class KMeansClustering:

    def __init__(self, k, data):
        self.k = k # Anzahl der Cluster/Mittelwertvektoren
        self.means = data[:k] # Mittelwertvektoren
        self.array = data # Array mit Daten
        self.groups = np.zeros(len(data)) # Clusterzugehörigkeit der Daten

    def calculate_means(self):
        # Hier bearbeiten und neue Mittelwertvektoren ermitteln
        self.means = [[0.] * len(self.array[0])] * self.k
        divider = [0] * self.k
        for i in range(len(self.array)):
            group = int(self.groups[i])
            divider[group] = divider[group] + 1
            self.means[group] = np.add(self.means[group], self.array[i]).tolist()

        for i in range(self.k):
            self.means[i] = np.divide(self.means[i], divider[i]).tolist()

    def cluster_data(self):
        # Ordnet die Daten den Clustern zu
        # Gibt False zurück, wenn die neu berechnete Ordnung der alten entspricht (Abbruchbedingung)
        new_groups = np.zeros(len(self.array))
        for i in range(len(self.array)):
            min_distance = -1
            for m in range(self.k):
                p_to_mean = np.subtract(self.array[i], self.means[m])
                distance = np.sum(np.multiply(p_to_mean, p_to_mean))
                if distance < min_distance or min_distance == -1:
                    min_distance = distance
                    new_groups[i] = m
        if np.array_equal(new_groups, self.groups):
            return False
        self.groups = new_groups
        return True

    def visualize(self):
        # Zeichnen der Plots
        for n in np.multiply(range(int(len(self.array[0])/2)), 2):
            plt.figure(n)
            for i in range(len(self.array)):
                category = self.groups[i]
                plt.plot(self.array[i][n], self.array[i][n+1], marker='o', color=self.get_color(category))
            for i in range(self.k):
                plt.plot(self.means[i][n], self.means[i][n+1], marker='x', color=self.get_color(i))
            if n == 0:
                plt.title("Sepal size")
                plt.ylabel("Sepal width (cm)")
                plt.xlabel("Sepal length (cm)")
            if n == 2:
                plt.title("Petal size")
                plt.ylabel("Petal width (cm)")
                plt.xlabel("Petal length (cm)")

        plt.show()

    def get_color(self, n):
        return (np.modf(1. / self.k * n)[0], np.modf(1. / self.k * 2 * n)[0],
              np.modf(1. / self.k * 3 * n)[0])


if __name__ == '__main__':
    # Läd Iris-Datensatz
    iris = datasets.load_iris()
    data_array = iris.data[:, :]
    # Erstellt eine KMeansClustering-Objekt mit k=3
    cluster = KMeansClustering(3, data_array)

    # K-Means Clustering Algorithmus nach Lloyd
    while cluster.cluster_data():
        cluster.calculate_means()

    cluster.visualize()