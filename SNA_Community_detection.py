from igraph import*
from math import floor
import pandas as pd
import os
import networkx as nx

G = nx.read_edgelist("test.edgelist", delimiter=" ")
g = Graph.from_networkx(G)
g.to_undirected()

leiden_membership = g.community_leiden(objective_function="modularity",n_iterations=50)
modularity = g.modularity(leiden_membership,directed=False)

vs = g.vs

members = leiden_membership.membership

id_nx = list(x for x in range(len(members)))

for i in range(len(id_nx)):
    id_nx[i] = vs[i]['_nx_name']

data = {"id": id_nx,
    'community': members}
DF = pd.DataFrame(data)

DF.to_csv("output.csv",index=False)