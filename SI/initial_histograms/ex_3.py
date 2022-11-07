import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

file = pd.read_csv('annuali.txt', delimiter = ";")
#print(file.head())
file_clean = file.drop(['Ora_rilevazione(GMT)'],axis=1).loc[(file.Grandezza != 'PRCPTOT - Precipitazioni totali giornaliere stimate - Totale annuale (mm)') & (file.Data_rilevazione != '01/01/2021')]
#print(file_clean.head())
df = file_clean.groupby(['Stazione'])

stations = []
for s in sorted(set(file_clean['Stazione'])):
    stations.append(df.get_group(s))

#stations e' una lista di dataframe, uno per stazione con pioggia tot e gg pioggia
# print(stations[0].head())
df_tot = []
df_gg = []
df_max = []
# import pdb; pdb.set_trace()
for i in range(len(stations)):
    if stations[i]['Valore'].apply(lambda x: '--' not in str(x)).all():
        df_tot.append(stations[i].loc[file_clean.Grandezza == 'Precipitazioni totali giornaliere - Totale annuale (mm)'])
        df_gg.append(stations[i].loc[file_clean.Grandezza == 'Giorni piovosi annuali (giorni mm>1) (%)'])
        df_max.append(stations[i].loc[file_clean.Grandezza == 'Precipitazioni totali giornaliere - Massima annuale (mm)'])

for i in range(len(df_tot)):
    if df_tot[i]['Stazione'].unique() == 'Siracusa':
        c = i
    if df_tot[i]['Stazione'].unique() == 'Palazzolo Acreide':
        p = i
    df_tot[i]['Valore'] = df_tot[i]['Valore'].astype(str).str.replace('--','0')
    df_gg[i]['Valore'] = df_gg[i]['Valore'].astype(str).str.replace('--','0')
    df_tot[i]['Valore'] = df_tot[i]['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
    df_gg[i]['Valore'] = df_gg[i]['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
    df_max[i]['Valore'] = df_max[i]['Valore'].astype(str).str.replace('--','0')
    df_max[i]['Valore'] = df_max[i]['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
# print(df_tot[0])
# print(df_gg[0])
m = []
for i in range(len(df_tot)):
    m.append(max(df_tot[i]['Valore']))
n = []
for i in range(len(df_gg)):
    n.append(max(df_gg[i]['Valore']))
o = []
for i in range(len(df_max)):
    o.append(max(df_max[i]['Valore']))
y1 = max(m)
y2 = max(n)
y3 = max(o)

fig, ax = plt.subplots(2,3)
l = []
for j in range(2009,2021):
    l.append(int(j))
x_axis = np.arange(2009,2021)

ax[0,0].bar(x_axis,df_tot[c]['Valore'],width=0.7,color='orange',tick_label=l)
ax[0,1].bar(x_axis,df_gg[c]['Valore'],width=0.7,color='green',tick_label=l)
ax[0,2].bar(x_axis, df_max[c]['Valore'],width=0.7, color='blue',tick_label=l)


ax[1,0].bar(x_axis,df_tot[p]['Valore'],width=0.7,color='orange',tick_label=l)
ax[1,1].bar(x_axis,df_gg[p]['Valore'],width=0.7,color='green',tick_label=l)
ax[1,2].bar(x_axis, df_max[p]['Valore'],width=0.7, color='blue',tick_label=l)

#ax[0,0].set_title('total')
ax[0,1].set_title('Siracusa')
#ax[0,2].set_title('maximum')

#ax[1,0].set_title('total')
ax[1,1].set_title('Palazzolo Acreide')
#ax[1,2].set_title('maximum')

ax[0,0].tick_params(axis='x', which='both', labelsize=7, labelrotation=90)
ax[0,1].tick_params(axis='x', which='both', labelsize=7, labelrotation=90)
ax[0,2].tick_params(axis='x', which='both', labelsize=7, labelrotation=90)

ax[1,0].tick_params(axis='x', which='both', labelsize=7, labelrotation=90)
ax[1,1].tick_params(axis='x', which='both', labelsize=7, labelrotation=90)
ax[1,2].tick_params(axis='x', which='both', labelsize=7, labelrotation=90)

ax[0,0].set_ylabel('total')
ax[0,1].set_ylabel('rainy days (%)')
ax[0,2].set_ylabel('maximum')

ax[1,0].set_ylabel('total')
ax[1,1].set_ylabel('rainy days (%)')
ax[1,2].set_ylabel('maximum')

ax[0,0].set_ylim([0,y1+1])
ax[0,1].set_ylim([0,y2+1])
ax[0,2].set_ylim([0,y3+1])

ax[1,0].set_ylim([0,y1+1])
ax[1,1].set_ylim([0,y2+1])
ax[1,2].set_ylim([0,y3+1])

fig.tight_layout()
plt.savefig('results/ex_3.png')