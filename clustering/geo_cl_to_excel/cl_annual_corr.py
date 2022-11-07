import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

directory = os.fsencode('../stations/')

years = []
for i in range(2009,2022):
	years.append(str(i))
years.sort()

for j in range(len(years)):
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

	files = {}
	for i in range(len(l)):
		files[l[i]] = pd.read_csv('../stations/'+l[i]+years[j]+'.txt', delimiter = ";")
		files[l[i]] = files[l[i]].replace(to_replace = '--', value='0')

	d = {}
	for item in files:
		d[item] = files[item]['Valore']
		d[item] = d[item].apply(lambda x: x.replace(',','.')).astype(float)
	df = pd.DataFrame(d)
	data = df.transpose()
	Y = data.to_numpy()
	Z = pdist(Y,metric = 'correlation')
	X = squareform(Z)
	clt = AffinityPropagation(damping=0.5, max_iter=500, affinity='precomputed')

	model = clt.fit(X)
	n_clusters = len(model.cluster_centers_indices_)
	print('Number of Clusters: ',n_clusters)

	clusters = pd.DataFrame(model.fit_predict(X))
	clusters = clusters.set_index(data.index)
	data = data.assign(cluster= clusters[0])
	print(data['cluster'])
	data['cluster'].to_excel('results/'+years[j]+'_corr.xlsx', sheet_name=years[j])
