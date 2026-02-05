import mpld3
from mpld3 import plugins
from mpld3.utils import get_id
import numpy as np
import collections
import matplotlib.pyplot as plt

N_paths = 5
N_steps = 100

x = np.linspace(0, 10, 100)
y = 0.1 * (np.random.random((N_paths, N_steps)) - 0.5)
y = y.cumsum(1)

fig, ax = plt.subplots()
labels = ["a", "b", "c", "d", "e"]
line_collections = ax.plot(x, y.T, lw=4, alpha=0.2)
interactive_legend = plugins.InteractiveLegendPlugin(line_collections, labels)
plugins.connect(fig, interactive_legend)

mpld3.display()