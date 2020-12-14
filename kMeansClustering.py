import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


class KMeansClustering:

    def __init__(self, k, data):
        self.k = k # Anzahl der Cluster/Mittelwertvektoren
        self.means = data[0:k] # Mittelwertvektoren
        self.array = data # Array mit Daten
        self.groups = np.zeros(len(data)) # Clusterzugehörigkeit der Daten

    def step(self):
        # Hier bearbeiten
        pass

    def optimal(self):
        new_groups = np.zeros(len(self.array))
        for i in range(len(self.array)):
            min_distance = -1
            for m in range(self.k):
                p_to_mean = [self.array[i][0] - self.means[m][0], self.array[i][1] - self.means[m][1]]
                distance = p_to_mean[0] * p_to_mean[0] + p_to_mean[1] * p_to_mean[1]
                if distance < min_distance or min_distance == -1:
                    min_distance = distance
                    new_groups[i] = m
        if np.array_equal(new_groups, self.groups):
            return True
        self.groups = new_groups
        return False

    def visualize(self):
        for i in range(len(self.array)):
            category = self.groups[i]
            plt.plot(self.array[i][0], self.array[i][1], marker='o', color=self.get_color(category))
        for i in range(self.k):
            plt.plot(self.means[i][0], self.means[i][1], marker='x', color=self.get_color(i))
        plt.show()

    def get_color(self, n):
        return (np.modf(1. / self.k * n)[0], np.modf(1. / self.k * 2 * n)[0],
              np.modf(1. / self.k * 3 * n)[0])


if __name__ == '__main__':
    iris = datasets.load_iris()
    data_array = iris.data[:, :2]
    cluster = KMeansClustering(3, data_array)

    while not cluster.optimal():
        cluster.step()

    if np.array_equal(cluster.groups, iris.target):
        print("Aufgabe erfolgreich beendet!")
    else:
        print("Da muss noch was getan werden!")

    cluster.visualize()
