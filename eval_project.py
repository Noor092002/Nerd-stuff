import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd
from sklearn.cluster import KMeans

eval_players = pd.read_csv(r"C:\Users\hp\Downloads\Gundogan Type Midfieder evaluation - Sheet8.csv")
eval_players.set_index("Name", inplace=True)

bld = eval_players['buildup']
att = eval_players['attack']
bld_att = np.column_stack((bld, att))
km_res = KMeans(n_clusters=3).fit(bld_att)
cluster = km_res.cluster_centers_
clust = km_res.labels_
eval_players['cluster'] = clust.tolist()


def findplyr():
    nm = str(input("Enter player name: ")) 
    inptclstr = eval_players.cluster[nm]
    smlrplyrs = eval_players[eval_players.cluster == inptclstr]

    return print(smlrplyrs)


findplyr()
