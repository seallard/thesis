import numpy as np
import matplotlib
from matplotlib import pyplot as plt


matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'lmodern',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

plt.figure(figsize=(2.5, 2))

data = [8093, 5119, 2274, 5317, 4802, 4533, 3211, 9817, 2042, 7336, 2142, 1720, 3626, 3506, 4751, 2282, 4521, 5648, 6587, 3747, 1433, 4134, 3242, 5499, 4817, 3400, 6351, 1799, 2892, 3470, 5308, 2873, 1140, 3966, 6099, 9614, 6258, 2075, 3652, 8933, 5868, 2654, 3700, 2297, 5357, 7231, 3241, 1523, 4590, 2673, 2627, 4392, 2713, 4857, 1427, 1689, 2489, 2478, 7378, 1974, 3867, 10745, 1533, 4948, 4645, 2576, 2733, 2668, 2815, 1039, 798, 7396, 4777, 1992, 3804, 6215, 1848, 2232, 3360, 5958, 3610, 1684, 3914, 2995, 1491, 2074, 5372, 2349, 1778, 14355, 2986, 4069, 4109, 4931, 3032, 2669, 2745, 3221, 8544, 3530]
bins = np.arange(0, 20000, 1000) # fixed bin size
plt.xlim([0, 20000])

plt.hist(data, bins=bins, alpha=0.8, edgecolor='black', linewidth=1.2)
plt.title('Evaluations until solved')
plt.xlabel('Networks evaluated')
plt.ylabel('Frequency')
plt.savefig('xor_evals.pgf', bbox_inches = "tight")



data = [4, 1, 2, 5, 1, 2, 4, 3, 1, 5, 1, 1, 3, 3, 3, 2, 1, 4, 4, 5, 3, 4, 3, 5, 3, 3, 5, 3, 3, 2, 5, 1, 2, 2, 4, 4, 3, 3, 2, 1, 2, 3, 7, 3, 9, 4, 5, 2, 3, 3, 2, 3, 2, 4, 3, 2, 2, 2, 4, 1, 2, 4, 2, 7, 3, 2, 2, 5, 3, 1, 1, 3, 4, 3, 3, 5, 3, 3, 3, 4, 1, 2, 3, 6, 2, 4, 5, 4, 1, 2, 4, 2, 2, 5, 1, 2, 3, 2, 2, 5]
bins = np.arange(0, max(data)+2, 1) # fixed bin size
plt.figure(figsize=(2.5, 2))
plt.xlim([0, max(data)+2])
plt.hist(data, bins=bins, alpha=0.8, edgecolor='black', linewidth=1.2)
plt.title('Hidden nodes')
plt.xlabel('Hidden nodes')
plt.ylabel('Frequency')

plt.savefig('xor_nodes.pgf', bbox_inches = "tight")


data = [15, 9, 10, 20, 11, 11, 14, 16, 9, 18, 7, 9, 12, 15, 14, 9, 9, 19, 16, 17, 10, 17, 13, 13, 14, 13, 19, 10, 14, 10, 17, 9, 10, 10, 19, 17, 17, 9, 11, 7, 13, 13, 17, 10, 25, 17, 14, 8, 16, 12, 11, 13, 8, 16, 10, 9, 12, 12, 20, 7, 15, 18, 7, 22, 16, 10, 8, 11, 12, 9, 7, 14, 12, 13, 13, 18, 12, 12, 13, 16, 9, 8, 15, 14, 10, 12, 19, 13, 7, 9, 12, 10, 8, 15, 7, 13, 12, 10, 14, 16]
bins = np.arange(max(data)-0.5) # fixed bin size
plt.figure(figsize=(2.5, 2))
plt.xlim([min(data)-2, max(data)+2])

plt.hist(data, bins=bins, alpha=0.8, edgecolor='black', linewidth=1.2)
plt.title('Number of links in networks solving XOR')
plt.xlabel('Links')
plt.ylabel('Frequency')

plt.savefig('xor_links.pgf', bbox_inches = "tight")