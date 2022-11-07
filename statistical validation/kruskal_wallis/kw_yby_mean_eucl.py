### KRUSKAL-WALLIS YEAR BY YEAR ###

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.mstats import kruskal

def check_equal_elements_in_list(l):
	v = []
	for i in range(len(l)-1):
			v.append(set(l[i])==set(l[i+1]))
	return all(v)

stats = ['agrigentomandrascava', 'alia', 'augusta', 'bivona', 'calascibetta',
    'caltagirone', 'caltanissetta', 'canicatti',
    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
    'palermo', 'paterno', 'pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
    'ramaccagiumarra', 'riesi', 'scicli', 'siracusa', 'trapanifontanasalsa']
s = {}
for y in range(2009,2022):
    df = pd.read_excel('../excel_recap/mean_eucl_clustering.xlsx', sheet_name=str(y))
    df.rename(columns={'Unnamed: 0': 'stations'}, inplace=True)    
    d = {}
    for cluster in df.groupby(['cluster']):
    	d[cluster[0]] = cluster[1]
    for cluster in df.groupby(['cluster']):   
    	f = {}
    	d[cluster[0]].reset_index(drop = True, inplace=True)
    	for col in d[cluster[0]].columns[2:-1]:
    		if col == 'violent rain (%)':
    			continue
    		f[col] = []
    		for i in range(len(d[cluster[0]][col])):
    			if col == 'intensity (mm/h)':
    				f[col].append(round(d[cluster[0]][col][i],2))
    			else:
    				f[col].append(d[cluster[0]][col][i])
    	d[cluster[0]] = f
    df = pd.DataFrame(d)
    df2 = df.T
    s[y] = df2

p_values_y = {}
for y in range(2009,2022):
	p_values = {}
	if len(s[y]) > 1: ### check if there are clusters ###
		for col in s[y].columns:
			l = []
			for elem in s[y][col]:
				l.append(elem)
			if check_equal_elements_in_list(l) == True: ### check if there are different values among clusters ###
				continue
			else:
				p_values[col] = round(kruskal(*l)[1],4)
	p_values_y[y] = p_values
p = pd.DataFrame(p_values_y).T
p.to_excel('results/y_p_values_mean_eucl.xlsx', sheet_name='year_by_year')
