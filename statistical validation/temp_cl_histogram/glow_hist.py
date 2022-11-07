import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')
stats = ['agrigentomandrascava', 'alia', 'augusta', 'bivona', 'calascibetta',
    'caltagirone', 'caltanissetta', 'canicatti',
    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
    'lascari', 'leni', 'marsala', 'messina', 'mineo', 'modica',
    'monrealebifarera', 'monrealevignaapi', 'mussomeli', 'palazzoloacreide',
    'palermo', 'paterno', 'pedara', 'pettineo', 'polizzigenerosa', 'ragusa',
    'ramaccagiumarra', 'riesi', 'scicli', 'siracusa', 'trapanifontanasalsa']
s = {}
l = []
h = []
for i in range(2009,2022):
	if i == 2009:
		stats = ['caltanissetta','contessaentellina','lascari','marsala', 'messina',
		'monrealevignaapi','palermo', 'pedara', 'pettineo', 'trapanifontanasalsa']
	elif i == 2010:
		stats = ['mussomeli', 'monrealevignaapi']
	elif i == 2011:
		stats = ['siracusa', 'paterno', 'riesi', 'ragusa']
	elif i == 2012:
		stats = ['bivona']
	elif i == 2013:
		stats = ['cesarovignazza','palazzoloacreide']
	elif i == 2014:
		stats = []
	elif i == 2015:
		stats = ['canicatti','catania', 'alia', 'augusta', 'caltagirone',
		'calascibetta','messina','leni','palazzoloacreide','monrealebifarera',
		'mineo','ramaccagiumarra','ragusa','polizzigenerosa','pettineo', 'pedara']
	elif i == 2016:
		stats = ['bivona','ragusa']
	elif i == 2017:
		stats = []
	elif i == 2018:
		stats = ['alia', 'calascibetta','canicatti',
    'catania', 'cesarovignazza', 'contessaentellina', 'enna', 'francofonte',
    'lascari', 'messina', 'mineo', 'modica',
    'monrealebifarera', 'monrealevignaapi', 'mussomeli',
    'pedara','polizzigenerosa',
    'ramaccagiumarra','scicli', 'siracusa']
	elif i == 2019:
		stats = ['caltagirone','calascibetta','mussomeli','polizzigenerosa']
	elif i == 2020:
		stats = ['catania','augusta','palermo']
	elif i == 2021:
		stats = ['catania','augusta','caltagirone','lascari','francofonte',
		'contessaentellina','monrealebifarera','monrealevignaapi','mineo',
		'siracusa']
	s[i] = []
	l.append(int(i))
	if stats == []:
		h.append(0)
	else:
		for stat in stats:
			df = pd.read_excel('../excel_recap/estations.xlsx', sheet_name=stat)
			df.rename(columns={'Unnamed: 0': 'years'}, inplace=True)
			s[i].append(df['heavy rain (%)'][int(i)-2009])
		h.append(np.mean(s[i]))
x_axis = np.arange(len(l))
ns = [int(9),int(2),int(4),int(1),int(1),int(0),int(17),int(2),int(0),int(20),int(3),int(3),int(10)]
width = 0.35
fig, ax = plt.subplots()

rects1 = ax.bar(x_axis, ns, width, tick_label=l, label = 'number of anomalies by year', color = 'orangered')
ax2 = ax.twinx()
rects2 = ax2.bar(x_axis + width, h, width, tick_label=l, label = 'heavy rain mean (%)', color ='steelblue')
ax.set_title('')
ax.tick_params(axis='x', which='both', labelsize=17, labelrotation=90)
ax.tick_params(axis='y', which='both', labelsize=17)
ax2.tick_params(axis='y', which='both', labelsize=17)
ax.set_ylim(0,20)
ax2.set_ylim(0,8)
ax.set_ylabel(r'counter')
ax2.set_ylabel(r'heavy rain (%)')
rects = [rects1, rects2]
labs = [l.get_label() for l in rects]
ax.legend(rects, labs, loc = 2, prop={'size': 17}, bbox_to_anchor=(0.0001, 1.33))

fig.tight_layout()
plt.savefig('results/final_a.pdf')

