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

	if j == 0: #2009
		stats = ['agrigentomandrascava', 'alia','augusta', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'mineo', 'modica',
	    'monrealebifarera', 'mussomeli', 'palazzoloacreide',
	    'paterno','pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 1: #2010
		stats = ['agrigentomandrascava', 'alia', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'mineo', 'modica',
	    'monrealebifarera', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 2: #2011
		stats = ['agrigentomandrascava', 'alia', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'messina', 'mineo',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli',
	    'palermo', 'pettineo', 'polizzigenerosa',
	    'ramaccagiumarra', 'riesi', 'scicli', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 3: #2012
		stats = ['agrigentomandrascava', 'alia','augusta', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'paterno','pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 4: #2013
		stats = ['agrigentomandrascava', 'alia','bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 
	    'palermo', 'paterno','pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 5: #2014
		stats = ['agrigentomandrascava', 'alia', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'enna', 'francofonte',
	    'lascari', 'marsala', 'messina', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli',
	    'palermo', 'paterno', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 6: #2015
		stats = ['agrigentomandrascava', 'alia', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'paterno', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa', 'trapanifontanasalsa']		
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 7: #2016
		stats = ['agrigentomandrascava', 'alia', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'catania', 'cesarovignazza', 'contessaentellina', 'francofonte',
	    'lascari', 'leni', 'marsala', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'paterno', 'pettineo', 'polizzigenerosa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 8: #2017
		stats = ['agrigentomandrascava', 'alia','augusta', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'messina', 'mineo',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'paterno','pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 9: #2018
		stats = ['agrigentomandrascava', 'alia','augusta', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'cesarovignazza', 'contessaentellina', 'francofonte',
	    'lascari', 'leni', 'marsala', 'messina', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'paterno', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 10: #2019
		stats = ['agrigentomandrascava', 'alia','augusta', 'bivona',
	    'caltanissetta', 'canicatti', 'catania',
	    'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'messina','mineo',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli',
	    'palermo', 'paterno','pedara','pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 11: #2020
		stats = ['agrigentomandrascava', 'alia','bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'paterno','pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli','siracusa', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	elif j == 12: #2021
		stats = ['agrigentomandrascava', 'alia', 'bivona', 'calascibetta',
	    'caltagirone', 'caltanissetta', 'canicatti',
	    'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
	    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
	    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
	    'palermo', 'paterno','pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
	    'ramaccagiumarra', 'riesi', 'scicli', 'trapanifontanasalsa']
		l = []
		for s in stats:
			l.append(s)
		l.sort()
	files = {}
	for i in range(len(l)):
		files[l[i]] = pd.read_csv('../stations/'+l[i]+years[j]+'.txt', delimiter = ";")
		files[l[i]].drop(['Grandezza', 'Stazione', 'Data rilevazione', 'Ora rilevazione'], axis=1, inplace = True)
		files[l[i]] = files[l[i]].replace(to_replace = '--', value='0')
		files[l[i]]['Valore'] = files[l[i]]['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
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
	data['cluster'].to_excel('results/'+years[j]+'_eucl_liv_2.xlsx', sheet_name=years[j])
