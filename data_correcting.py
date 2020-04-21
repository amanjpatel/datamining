# samples and plots connections from sparse npz connectivity files that have been reformatted into two lists:
# one contains the presynaptic neuron, one contains the postsynaptic neuron, at each index.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

file_name_load = input("what file do you want to load?")

# load the file
data = np.load(file_name_load)
conxns = data['arr_0']
print(conxns)
# print(np.count_nonzero(conxns[0] == 1361332))

# create variables to hold file data
# length of both = 25714382
presyn = conxns[0]
postsyn = conxns[1]

# empty sample lists
samp_pre = []
samp_post = []

#sample the first 10000 out of all connections
samp_cutoff = input('The sample to be graphed is the first ____ connections? type len(presyn) for all:')

# create samples
for x in range(0, int(samp_cutoff)):
    samp_pre.append(presyn[x])
    samp_post.append(postsyn[x])
print(samp_pre)
print(samp_post)

# add nodes to graph
g = nx.MultiDiGraph()
g.add_nodes_from(samp_pre[:])
g.add_nodes_from(samp_post[:])

# add edges to graph
for x in range(0, len(samp_pre)):
    g.add_edge(samp_pre[x], samp_post[x])

# draw graph, save figure, plot graph, save graph data
nx.draw(g)
# plt.savefig('thousand_neuron_net')
plt.show()
# nx.write_gexf(g, 'ECT_local_graph')