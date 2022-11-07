import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

####REMOVE 29/02 FROM LEAP YEARS####
directory = os.fsencode('../annual_mean_stations/') 
stats = ['agrigentomandrascava', 'alia', 'augusta', 'bivona', 'calascibetta',
    'caltagirone', 'caltanissetta', 'canicatti',
    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
    'palermo', 'paterno', 'pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
    'ramaccagiumarra', 'riesi', 'scicli', 'siracusa', 'trapanifontanasalsa']

for stat in stats:
	l = []
	for s in os.listdir(directory):
		s = s.decode('ascii')
		if s.startswith(stat):
			l.append(s)
	l.sort()

	files = {}
	for i in range(len(l)):
		files[l[i]] = pd.read_csv('../annual_mean_stations/'+l[i], delimiter = ";")
		files[l[i]].drop(['Unnamed: 0'], axis=1, inplace = True)
		files[l[i]] = files[l[i]].replace(to_replace = '--', value='0')
	d = {}
	for item in files:
		d[item[-8:-4]] = files[item]['0']
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
	tab = data['cluster']
	tab2 = pd.DataFrame(tab)
	tab2.to_excel('results/mean_eucl_'+stat+'.xlsx', sheet_name=stat)
