import pandas as pd
import os
import numpy as np

directory = os.fsencode('../stations/')

years = []
for i in range(2009,2022):
	years.append(str(i))
years.sort()

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
	for k in range(len(l2[j])):
		files.append(pd.read_csv('../tations/'+l2[j][k], delimiter = ";"))
		file_clean = files[k].replace(to_replace = '--', value='0')
		file_clean['Data rilevazione'] = file_clean[file_clean.columns[2:4]].apply(
    	lambda x: ','.join(x.astype(str)),
    	axis=1)
		df = file_clean.drop(['Ora rilevazione', 'Grandezza', 'Stazione'], axis=1)
		df['Valore'] = df['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
		step = 1008
		df_steps = []
		for i in range((len(df)//step)+1):
			df_steps.append(df.iloc[(i*step):((i+1)*step)+1])
		means = []
		for i in range(len(df_steps)):
			means.append(round(df_steps[i]['Valore'].mean(),3))
		m = pd.DataFrame(means)
		m.to_csv('../annual_mean_stations/'+l2[j][k], sep=';', mode='a')
