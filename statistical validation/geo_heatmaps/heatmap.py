import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np

year = input("Please enter a year from 2009 to 2021 or global:\n")
indicator = input ("Please enter the indicator you want to plot:\n Choose between: light rain (%), moderate rain (%), heavy rain (%),\n violent rain, max daily variation, maximum (per hour), total,\n maximum (per day), wet days (%), intensity (mm/h),\n wet hours (%):\n")
sicily = gpd.read_file('../../clustering/geo_cl_to_map/sicilia/sicilia.shp')
ax = sicily.plot(figsize=(10, 10))
x=[913000,923000,1043500,894300,971300,990000,947800,932800,
1035600,1000800,857800,962300,1019400,932300,1009000,
818800,1071800,1007200,1021100,885800,874700,
927900,1023100,879300,1021500,1038500,970700,
947900,1018100,1002200,955900,1011800,1052200,811200]
y=[4133185,4193185,4142000,4163600,4188000,4141000,4165200,
4139900,4169000,4210000,4175200,4177700,4133900,4215900,
4283700,4195100,4255800,4147900,4096400,4201100,4223800,
4172100,4116700,4234500,4177800,4181800,4215100,
4201500,4103300,4160100,4124800,4082900,4121100,4207100]
s = ['Agrigento Mandrascava', 'Alia', 'Augusta', 'Bivona', 'Calascibetta',
'Caltagirone', 'Caltanissetta', 'Canicatti',
'Catania', 'Cesaro Vignazza', 'Contessa Entellina', 'Enna', 'Francofonte',
'Lascari', 'Leni', 'Marsala', 'Messina', 'Mineo', 'Modica',
'Monreale Bifarera', 'Monreale Vigna Api', 'Mussomeli', 'Palazzolo Acreide',
'Palermo', 'Paterno', 'Pedara', 'Pettineo', 'Polizzi Generosa', 'Ragusa',
'Ramacca Giumarra', 'Riesi', 'Scicli', 'Siracusa', 'Trapani Fontanasalsa']

for i, txt in enumerate(s):
	ax.text(x=x[i]-4000,y=y[i]-6000,s=txt, 
		fontdict=dict(color='black',size=11))
ax.set_xlim(800000, 1100000)
ax.set_ylim(4070000, 4300000)


df = pd.read_excel('../excel_recap/mean_eucl_clustering.xlsx',sheet_name=str(year))
df.rename(columns={'Unnamed: 0': 'stations'}, inplace=True)
ind = df[indicator]
scatter = ax.scatter(x,y, alpha=0.7, s=700,c = ind, cmap = 'inferno')
# ax.set_title(str(indicator)+' - '+str(year))
norm = mpl.colors.Normalize(vmin=0,vmax=max(ind))
sm = plt.cm.ScalarMappable(cmap='inferno', norm=norm)
sm.set_array([])
N = len(set(ind))
if max(ind) < 20:
	plt.colorbar(sm, ticks=np.linspace(0,round(max(ind)),round(max(ind))+1),
	boundaries=np.arange(-0.05,max(ind)+0.2,.1), fraction=0.035, pad=0.04).set_label(label=str(indicator),size=18,weight='bold')
else:
	plt.colorbar(sm, ticks=np.linspace(0,round(max(ind)),11),
	boundaries=np.arange(-0.05,round(max(ind))+11,11), fraction=0.035, pad=0.04).set_label(label=str(indicator),size=18,weight='bold')
ax.axis('off')
plt.savefig('results/'+indicator+'_sicilia_'+ str(year)+'.pdf', dpi = 600)
