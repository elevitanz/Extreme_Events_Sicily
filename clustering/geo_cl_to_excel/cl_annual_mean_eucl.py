import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

directory = os.fsencode('../annual_mean_stations/')
stats = ['agrigentomandrascava', 'alia','augusta', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'paterno','pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa', 'trapanifontanasalsa']

l = []
for s in stats:
	l.append(s)
l.sort()
for y in range(2009,2022):
	year = str(y)
	files = {}
	for stat in stats:
		files[stat] = pd.read_csv('../annual_mean_stations/'+stat+year+'.txt', delimiter = ";")
		files[stat].drop(['Unnamed: 0'], axis=1, inplace = True)

	d = {}
	for item in files:
		d[item] = files[item]['0']
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
	data['cluster'].to_excel('results/'+year+'_mean_eucl.xlsx', sheet_name=year)