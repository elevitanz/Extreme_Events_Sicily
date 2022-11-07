import os
import numpy as np
import pandas as pd

directory = os.fsencode('../../clustering/stations/') 
stats = ['agrigentomandrascava', 'alia', 'augusta', 'bivona', 'calascibetta',
    'caltagirone', 'caltanissetta', 'canicatti',
    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
    'palermo', 'paterno', 'pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
    'ramaccagiumarra', 'riesi', 'scicli', 'siracusa', 'trapanifontanasalsa']

def wet_days(df):
	c = 0
	step = 144
	for i in range(len(df)//step):
		s = 0.0
		for j in range(i* step,(i+1)*step+1):
			s += df['Valore'][j]
		if s > 1.0:
			c+=1
			continue
		else:
			continue
	return c

def maxim(df):
	step = 144
	l = []
	for i in range(len(df)//step):
		s = 0.0
		for j in range(i* step,(i+1)*step+1):
			s += df['Valore'][j]
		l.append(round(s,2))
	return max(l)

def total(df):
	s = 0.0
	for i in range(len(df)):
		s += df['Valore'][i]
	return round(s,2)

def rain_per_hour(df):
	step = 6
	l = []
	for i in range(len(df)//step):
		s = 0.0
		for j in range(i* step,(i+1)*step+1):
			s += df['Valore'][j]
		l.append(round(s,2))
	return l

def categories(df):
	tot = 0
	light = 0
	moderate = 0
	heavy = 0
	violent = 0
	for elem in rain_per_hour(df):
		if elem != 0.0:
			tot += 1
			if elem <= 2.5:
				light += 1
			elif elem > 2.5 and elem <= 7.5:
				moderate += 1
			elif elem > 7.5 and elem <= 50.0:
				heavy += 1
			elif elem > 50.0:
				violent += 1
	return {'light rain hours': light,
			'moderate rain hours': moderate,
			'heavy rain hours': heavy,
			'violent rain hours': violent,
			'tot': tot}

def total_rain_per_day(df):
	step = 144
	l = []
	for i in range(len(df)//step):
		s = 0.0
		for j in range(i* step,(i+1)*step+1):
			s += df['Valore'][j]
		l.append(round(s,2))
	return l

def max_var(df):
	v = []
	l = total_rain_per_day(df)
	for i in range(len(l)-1):
			v.append(round(abs(l[i]-l[i+1]),2))
	return max(v)

for stat in stats:
	indicators = {}
	for i in range(2009,2022):
		indicators[i] = []
		file = pd.read_csv('../../clustering/stations/'+stat+str(i)+'.txt', delimiter = ";")
		file_clean = file.replace(to_replace = '--', value='0')
		file_clean['Data rilevazione'] = file_clean[file_clean.columns[2:4]].apply(
    		lambda x: ','.join(x.astype(str)),
    		axis=1)
		df = file_clean.drop(['Ora rilevazione', 'Grandezza', 'Stazione'], axis=1)
		df['Valore'] = df['Valore'].apply(lambda x: x.replace(',','.')).astype(float)	
		if i != 2012 and i != 2016 and i!= 2020:
			perc_days = round((wet_days(df))*100/365)
			perc_tot = round((categories(df)['tot'])*100/(365*24))
		else:
			perc_days = round((wet_days(df))*100/366)
			perc_tot = round((categories(df)['tot'])*100/(366*24))
		indicators[i].append(perc_days)
		indicators[i].append(intensity)
		indicators[i].append(maxim(df))
		indicators[i].append(total(df))
		indicators[i].append(max(rain_per_hour(df))) ###max per hour (mm)
	
		perc_light = round((categories(df)['light rain hours'])*100/(categories(df)['tot']))
		perc_moderate = round((categories(df)['moderate rain hours'])*100/(categories(df)['tot']))	
		perc_heavy = round((categories(df)['heavy rain hours'])*100/(categories(df)['tot']))		
		violent = round((categories(df)['violent rain hours']))	
	
		indicators[i].append(perc_light) ###perc of light rain hours
		indicators[i].append(perc_moderate) ###perc of moderate rain hours
		indicators[i].append(perc_heavy) ###perc of heavy rain hours
		indicators[i].append(violent) ###perc of violent rain hours
		indicators[i].append(perc_tot) ###perc of wet hours
		indicators[i].append(max_var(df)) ###max var

	ind = pd.DataFrame(indicators).T
	ind.rename(columns={0: 'wet days (%)',
					1: 'maximum (per day)',
					2: 'total',
					3: 'maximum (per hour)',
					4: 'light rain (%)',
					5: 'moderate rain (%)',
					6: 'heavy rain (%)',
					7: 'violent rain (%)',
					8: 'wet hours (%)',
					9: 'max daily variation'}, inplace=True)
	ind.to_excel('results/'+stat+'.xlsx', sheet_name=stat)
