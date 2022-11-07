import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd

sicily = gpd.read_file('sicilia/sicilia.shp')
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
    'Caltagirone', 'Caltanissetta', 'Canicattì',
    'Catania', 'Cesarò Vignazza', 'Contessa Entellina', 'Enna', 'Francofonte',
    'Lascari', 'Leni', 'Marsala', 'Messina', 'Mineo', 'Modica',
    'Monreale Bifarera', 'Monreale Vigna Api', 'Mussomeli', 'Palazzolo Acreide',
    'Palermo', 'Paternò', 'Pedara', 'Pettineo', 'Polizzi Generosa', 'Ragusa',
    'Ramacca Giumarra', 'Riesi', 'Scicli', 'Siracusa', 'Trapani Fontanasalsa']
ax.scatter(913000,4133185, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(923000,4193185, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1043500,4142000, marker=".", color='orange', alpha=0.7, zorder=5, s=100)
ax.scatter(894300,4163600, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(971300,4188000, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(990000,4141000, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(947800,4165200, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(932800,4139900, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1035600,4169000, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1000800,4210000, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(857800,4175200, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(962300,4177700, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1019400,4133900, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(932300,4215900, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1009000,4283700, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(818800,4195100, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1071800,4255800, marker="D", color='r', alpha=0.7, zorder=5, s=100)
ax.scatter(1007200,4147900, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1021100,4096400, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(885800,4201100, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(874700,4223800, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(927900,4172100, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1023100,4116700, marker="s", color='aqua', alpha=0.7, zorder=5, s=40)
ax.scatter(879300,4234500, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1021500,4177800, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1038500,4181800, marker=".", color='lime', alpha=0.7, zorder=5, s=100)
ax.scatter(970700,4215100, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(947900,4201500, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1018100,4103300, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1002200,4160100, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(955900, 4124800, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1011800, 4082900, marker=".", color='b', alpha=0.7, zorder=5, s=100)
ax.scatter(1052200, 4121100, marker=".", color='purple', alpha=0.7, zorder=5, s=100)
ax.scatter(811200,4207100, marker=".", color='b', alpha=0.7, zorder=5, s=100)
for i, txt in enumerate(s):
	ax.text(x=x[i]-4000,y=y[i]-6000,s=txt, 
          fontdict=dict(color='black',size=7))
plt.savefig('results/global_eucl_c'+'.png', dpi = 200)
