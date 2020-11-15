#!/usr/bin/python3

#
# Definiert die optimal benoetigten Steps fuer die 11_17 Gridworld
#
#  direkt ./step_count_env_11_17.py aufrufen
#
# tas 10.11.2020
#

import numpy as np
import matplotlib.pylab as plt

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16
stepcounts = np.array([
[ 5, 4, 3, 2, 1,-2, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11],
[ 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12],
[ 7, 6,-1, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13],
[ 8, 7,-1, 5,-1,-1,-1,-1,-1, 7,-1,-1,-1,11,12,13,14],
[ 9, 8,-1, 6, 7, 8, 9,10, 9, 8, 9,10,11,12,13,14,15],
[10, 9,-1, 7, 8, 9,10,11,10, 9,10,11,12,13,14,15,16],
[11,10,-1, 8, 9,10,11,12,11,10,11,12,13,14,15,16,17],
[12,11,-1, 9,10,11,12,13,12,11,12,13,14,15,16,17,18],
[13,12,-1,10,11,12,13,14,13,12,13,14,15,16,17,18,19],
[14,13,12,11,12,13,14,15,14,13,14,15,16,17,18,19,20],
[15,14,13,12,13,14,15,16,15,14,15,16,17,18,19,20,21]
])

print("Script wird beendet, wenn die Grafik geschlossen wird.")
plt.matshow(stepcounts)
plt.show()
