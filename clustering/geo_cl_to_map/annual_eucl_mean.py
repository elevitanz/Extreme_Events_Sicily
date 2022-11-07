import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd

for year in range(2009,2022):
	df = pd.read_excel('../geo_cl_to_excel/results/'+str(year)+'_mean_eucl.xlsx',sheet_name=str(year))
	df.rename(columns={'Unnamed: 0': 'stations'}, inplace=True)
	colors = ['blue', 'red', 'yellow', 'lime', 'aqua', 'navy', 'purple', 'deeppink', 'sienna', 'olivedrab', 'orange', 'grey']
	colors = colors[:len(set(df['cluster']))]
	sicily = gpd.read_file('sicilia/sicilia.shp')
	ax = sicily.plot(figsize=(10, 10))
	x=[913000,923000,1043500,894300,971300,990000,947800,932800,
	1035600,1000800,857800,962300,1019400,932300,
	1025100,818800,1071800,1007200,1021100,885800,874700,
	927900,1023100,879300,1021500,1038500,970700,
	947900,1018100,1002200,955900,1011800,1052200,811200]
	y=[4133185,4193185,4142000,4163600,4188000,4141000,4165200,
	4139900,4169000,4210000,4175200,4177700,4133900,4215900,
	4283700,4195100,4255800,4147900,4096400,4201100,4223800,
	4172100,4116700,4234500,4177800,4181800,4215100,
	4201500,4103300,4160100,4124800,4082900,4121100,4207100]
	s = ['Agrigento Mandrascava', 'Alia', 'Augusta', 'Bivona', 'Calascibetta',
    'Caltagirone', 'Caltanissetta', 'Canicattì',
    'Catania', 'Cesarò Vignazza', 'Contessa Entellina', 'Enna', 'Francofonte',
    'Lascari', 'Leni', 'Marsala', 'Messina', 'Mineo', 'Modica',
    'Monreale Bifarera', 'Monreale Vigna Api', 'Mussomeli', 'Palazzolo Acreide',
    'Palermo', 'Paternò', 'Pedara', 'Pettineo', 'Polizzi Generosa', 'Ragusa',
    'Ramacca Giumarra', 'Riesi', 'Scicli', 'Siracusa', 'Trapani Fontanasalsa']
	#agrig
	ax.scatter(913000,4133185, marker=".", color=colors[df['cluster'].loc[0]], alpha=0.7, zorder=5, s=100)
	#alia
	ax.scatter(923000,4193185, marker=".", color=colors[df['cluster'].loc[1]], alpha=0.7, zorder=5, s=100)
	#aug
	ax.scatter(1043500,4142000, marker=".", color=colors[df['cluster'].loc[2]], alpha=0.7, zorder=5, s=100)
	#biv
	ax.scatter(894300,4163600, marker=".", color=colors[df['cluster'].loc[3]], alpha=0.7, zorder=5, s=100)
	#calasc
	ax.scatter(971300,4188000, marker=".", color=colors[df['cluster'].loc[4]], alpha=0.7, zorder=5, s=100)
	#caltag
	ax.scatter(990000,4141000, marker=".", color=colors[df['cluster'].loc[5]], alpha=0.7, zorder=5, s=100)
	#caltaniss
	ax.scatter(947800,4165200, marker=".", color=colors[df['cluster'].loc[6]], alpha=0.7, zorder=5, s=100)
	#canicat
	ax.scatter(932800,4139900, marker=".", color=colors[df['cluster'].loc[7]], alpha=0.7, zorder=5, s=100)
	#ct
	ax.scatter(1035600,4169000, marker=".", color=colors[df['cluster'].loc[8]], alpha=0.7, zorder=5, s=100)
	#cesaro
	ax.scatter(1000800,4210000, marker=".", color=colors[df['cluster'].loc[9]], alpha=0.7, zorder=5, s=100)
	#contessa
	ax.scatter(857800,4175200, marker=".", color=colors[df['cluster'].loc[10]], alpha=0.7, zorder=5, s=100)
	#enna
	ax.scatter(962300,4177700, marker=".", color=colors[df['cluster'].loc[11]], alpha=0.7, zorder=5, s=100)
	#francofonte
	ax.scatter(1019400,4133900, marker=".", color=colors[df['cluster'].loc[12]], alpha=0.7, zorder=5, s=100)
	#lascari
	ax.scatter(932300,4215900, marker=".", color=colors[df['cluster'].loc[13]], alpha=0.7, zorder=5, s=100)
	#leni
	ax.scatter(1009000,4283700, marker=".", color=colors[df['cluster'].loc[14]], alpha=0.7, zorder=5, s=100)
	#marsala
	ax.scatter(818800,4195100, marker=".", color=colors[df['cluster'].loc[15]], alpha=0.7, zorder=5, s=100)
	#messina
	ax.scatter(1071800,4255800, marker=".", color=colors[df['cluster'].loc[16]], alpha=0.7, zorder=5, s=100)
	#mineo
	ax.scatter(1007200,4147900, marker=".", color=colors[df['cluster'].loc[17]], alpha=0.7, zorder=5, s=100)
	#modica
	ax.scatter(1021100,4096400, marker=".", color=colors[df['cluster'].loc[18]], alpha=0.7, zorder=5, s=100)
	#bif
	ax.scatter(885800,4201100, marker=".", color=colors[df['cluster'].loc[19]], alpha=0.7, zorder=5, s=100)
	#vignaapi
	ax.scatter(874700,4223800, marker=".", color=colors[df['cluster'].loc[20]], alpha=0.7, zorder=5, s=100)
	#mussomeli
	ax.scatter(927900,4172100, marker=".", color=colors[df['cluster'].loc[21]], alpha=0.7, zorder=5, s=100)
	#palazz
	ax.scatter(1023100,4116700, marker=".", color=colors[df['cluster'].loc[22]], alpha=0.7, zorder=5, s=100)
	#palermo
	ax.scatter(879300,4234500, marker=".", color=colors[df['cluster'].loc[23]], alpha=0.7, zorder=5, s=100)
	#paterno
	ax.scatter(1021500,4177800, marker=".", color=colors[df['cluster'].loc[24]], alpha=0.7, zorder=5, s=100)
	#pedara
	ax.scatter(1038500,4181800, marker=".", color=colors[df['cluster'].loc[25]], alpha=0.7, zorder=5, s=100)
	#pettineo
	ax.scatter(970700,4215100, marker=".", color=colors[df['cluster'].loc[26]], alpha=0.7, zorder=5, s=100)
	#polizzi
	ax.scatter(947900,4201500, marker=".", color=colors[df['cluster'].loc[27]], alpha=0.7, zorder=5, s=100)
	#ragusa
	ax.scatter(1018100,4103300, marker=".", color=colors[df['cluster'].loc[28]], alpha=0.7, zorder=5, s=100)
	#ramacca
	ax.scatter(1002200,4160100, marker=".", color=colors[df['cluster'].loc[29]], alpha=0.7, zorder=5, s=100)
	#riesi
	ax.scatter(955900, 4124800, marker=".", color=colors[df['cluster'].loc[30]], alpha=0.7, zorder=5, s=100)
	#scicli
	ax.scatter(1011800, 4082900, marker=".", color=colors[df['cluster'].loc[31]], alpha=0.7, zorder=5, s=100)
	#siracusa
	ax.scatter(1052200, 4121100, marker=".", color=colors[df['cluster'].loc[32]], alpha=0.7, zorder=5, s=100)
	#trapani
	ax.scatter(811200,4207100, marker=".", color=colors[df['cluster'].loc[33]], alpha=0.7, zorder=5, s=100)

	for i, txt in enumerate(s):
		ax.text(x=x[i]-4000,y=y[i]-6000,s=txt, 
	          fontdict=dict(color='black',size=7))
	plt.savefig('results/eucl_mean_clustering'+str(year)+'.png', dpi = 600)