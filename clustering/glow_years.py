import pandas as pd
import os
import numpy as np

directory = os.fsencode('../stations/') 
l = []

for s in os.listdir(directory):
	s = s.decode('ascii')
	l.append(s)

l.sort()
l2 = []
splits = np.array_split(l[1:], 38)
for array in splits:
	s = list(array)
	l2.append(s)

for j in range(len(l2)):
	files = []
	
	for i in range(len(l2[j])):
		files.append(pd.read_csv('../stations/'+l2[j][i], delimiter = ";"))
	
	merged_file = pd.concat(files, axis=0, ignore_index = True)
	file_clean = merged_file.replace(to_replace = '--', value='0')
	file_clean['Data rilevazione'] = file_clean[file_clean.columns[2:4]].apply(
    	lambda x: ','.join(x.astype(str)),
    	axis=1)
	df = file_clean.drop(['Ora rilevazione', 'Grandezza'], axis=1)
	df['Valore'] = df['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
	df.drop_duplicates(inplace=True, ignore_index = True)
	df.to_csv('../global_stations/'+l2[j][0][:-8], sep=';', mode='a')
