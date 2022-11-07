import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

file = pd.read_csv('annuali.txt', delimiter = ";")
file_clean = file.drop(['Ora_rilevazione(GMT)'],axis=1).loc[(file.Grandezza != 'PRCPTOT - Precipitazioni totali giornaliere stimate - Totale annuale (mm)') & (file.Data_rilevazione != '01/01/2021')]
df = file_clean.groupby(['Stazione'])

stations = []
for s in set(file_clean['Stazione']):
    stations.append(df.get_group(s))

df_tot = []
df_gg = []
df_max = []
for i in range(len(stations)):
    if stations[i]['Valore'].apply(lambda x: '--' not in str(x)).all():
        df_tot.append(stations[i].loc[file_clean.Grandezza == 'Precipitazioni totali giornaliere - Totale annuale (mm)'])
        df_gg.append(stations[i].loc[file_clean.Grandezza == 'Giorni piovosi annuali (giorni mm>1) (%)'])
        df_max.append(stations[i].loc[file_clean.Grandezza == 'Precipitazioni totali giornaliere - Massima annuale (mm)'])

av_gg = []
av_max = []
for i in range(len(df_tot)):
    df_tot[i]['Valore'] = df_tot[i]['Valore'].astype(str).str.replace('--','0')
    df_gg[i]['Valore'] = df_gg[i]['Valore'].astype(str).str.replace('--','0')
    df_tot[i]['Valore'] = df_tot[i]['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
    df_gg[i]['Valore'] = df_gg[i]['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
    df_max[i]['Valore'] = df_max[i]['Valore'].astype(str).str.replace('--','0')
    df_max[i]['Valore'] = df_max[i]['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
    av_max.append(round(sum(df_max[i]['Valore'])/12))
    av_gg.append(round(sum(df_gg[i]['Valore'])/12))

def extreme_events(df_max,df_gg,av_max,av_gg):
    if df_max >= av_max and df_gg <= av_gg:
        return True
    else:
        return False

L = []
for i in range(len(df_tot)):
    for year in range(2009,2021):
        L.append([str(df_tot[i]['Stazione'].loc[df_tot[i]['Stazione'].index[0]]),year,extreme_events(df_max[i]['Valore'].reset_index(drop=True)[year-2009], df_gg[i]['Valore'].reset_index(drop=True)[year-2009], av_max[i], av_gg[i])])
df = pd.DataFrame(L, columns =['Station', 'Year', 'Extreme event'])
impo = pd.pivot_table(df,index=['Station'], columns = ['Year']).astype(bool)
impo.to_excel("results/tab_med.xlsx")
