import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

file = pd.read_csv('../stations/augusta2020.txt', delimiter = ";")
file_clean = file.replace(to_replace = '--', value='0')
file_clean['Data rilevazione'] = file_clean[file_clean.columns[2:4]].apply(
    lambda x: ','.join(x.astype(str)),
    axis=1)
df = file_clean.drop(['Ora rilevazione', 'Grandezza', 'Stazione'], axis=1)
df['Valore'] = df['Valore'].apply(lambda x: x.replace(',','.')).astype(float)
def dry_days(df):
	l = []
	c = 0
	for j in range(len(df)):
		if df['Valore'][j] == 0.0:
			c+=1
		else:
			l.append(c)
			c = 0
			continue
	l.append(c)
	return round(max(l)/144)

def wet_hours(df):
	l = []
	c = 0
	for j in range(len(df)):
		if df['Valore'][j] != 0.0:
			c+=1
			continue
		else:
			if c != 0:
				l.append(c)
				c = 0
			continue
	l.append(c)
	return round(max(l)/6)

months = [0, 4464, 8640, 13104, 17424, 21888, 26208, 30672, 35136, 39456, 43920, 48240, 52704] 
df_months = []

for i in range(len(months)-1):
	df_months.append(df.iloc[months[i]:months[i+1]+1])

dry = []
wet = []
for i in range(len(df_months)):	
	month = df_months[i]['Data rilevazione'].loc[df_months[i]['Data rilevazione'].index[0]][3:10]
	month = month.replace('/', '-')
	dry.append(dry_days(df_months[i].reset_index()))
	wet.append(wet_hours(df_months[i].reset_index()))
	df_months[i]['Valore'].plot()
	plt.text(0.02, 0.96,'Max dry days:'+ str(dry[-1]), fontsize=10,bbox = dict(facecolor = 'blue', alpha = 0.5), transform=plt.gcf().transFigure)
	plt.text(0.02, 0.9,'Max wet hours:'+ str(wet[-1]), fontsize=10,bbox = dict(facecolor = 'blue', alpha = 0.5), transform=plt.gcf().transFigure)
	plt.xlabel('time line - 10 min intervals')
	plt.ylabel('rain - mm')
	plt.title(str(file_clean['Stazione'].loc[file_clean['Stazione'].index[0]])+' ' +month)
	plt.ylim(top=22)
	plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	plt.savefig('results/'+str(file_clean['Stazione'].loc[file_clean['Stazione'].index[0]])+month+'.png')
	plt.show()