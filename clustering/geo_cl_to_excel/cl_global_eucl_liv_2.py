import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

directory = os.fsencode('../global_stations/')
stats = ['agrigentomandrascava', 'alia', 'bivona', 'calascibetta',
    'caltagirone', 'caltanissetta', 'canicatti',
    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
    'palermo', 'paterno', 'pettineo', 'polizzigenerosa', 'ragusa',
    'ramaccagiumarra', 'riesi', 'scicli', 'trapanifontanasalsa']

files = {}
for stat in stats:
	files[stat] = pd.read_csv('../global_stations/'+stat, delimiter = ";")
	files[stat].drop(['Unnamed: 0', 'Stazione', 'Data rilevazione'], axis=1, inplace = True)
d = {}
for item in files:
	d[item] = files[item]['Valore']
df = pd.DataFrame(d)
data = df.transpose()
X = data.to_numpy()
clt = AffinityPropagation(damping=0.5, max_iter=500, affinity='euclidean')
model = clt.fit(X)
n_clusters = len(model.cluster_centers_indices_)
print('Number of Clusters: ',n_clusters)

clusters = pd.DataFrame(model.fit_predict(X))
clusters = clusters.set_index(data.index)
data = data.assign(cluster= clusters[0])
print(data['cluster'])
data['cluster'].to_excel('results/global_eucl_liv_2.xlsx', sheet_name='global')
