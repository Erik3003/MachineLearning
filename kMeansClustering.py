import numpy as np
import matplotlib.pyplot as plt


class KMeansClustering:

    def __init__(self, k, data):
        self.k = k
        self.means = data[0:k]
        self.array = data
        self.groups = np.zeros(len(data))

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
    data_array = [[23., 11.], [3., 12.], [12., 8.], [23., 9.], [12., 9.], [10., 10.], [7., 4.], [20., 1.], [7., 11.]]
    cluster = KMeansClustering(3, data_array)

    while not cluster.optimal():
        cluster.step()

    cluster.visualize()