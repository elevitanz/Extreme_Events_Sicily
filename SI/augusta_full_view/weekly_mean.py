import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

directory = os.fsencode('../stations/') 
l = []
for s in os.listdir(directory):
	s = s.decode('ascii')
	if s.startswith('augusta'):
		l.append(s)
l.sort()
files = []
for i in range(len(l)):
	files.append(pd.read_csv('../stations/'+l[i], delimiter = ";"))
merged_file = pd.concat(files, axis=0, ignore_index = True)
file_clean = merged_file.replace(to_replace = '--', value='0')
file_clean['Data rilevazione'] = file_clean[file_clean.columns[2:4]].apply(
    lambda x: ','.join(x.astype(str)),
    axis=1)
df = file_clean.drop(['Ora rilevazione', 'Grandezza', 'Stazione'], axis=1)
df['Valore'] = df['Valore'].apply(lambda x: x.replace(',','.')).astype(float)

def dry_days(df):
	l = []
	c = 0
	for i in range(len(df)):
		if df['Valore'][i] == 0.0:
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
	for i in range(len(df)):
		if df['Valore'][i] != 0.0:
			c+=1
			continue
		else:
			if c != 0:
				l.append(c)
				c = 0
			continue
	l.append(c)
	return round(max(l)/6)

dry_days = dry_days(df)
wet_hours = wet_hours(df)
years = [0, 52560, 105121, 157682, 210387, 262948, 315509, 368070, 420775, 473336, 525897, 578458, 631163, 683725] 
df_years = []
x = [i*1008 for i in range(678)]
x.append(683725)
step = 1008
df_steps = []
for i in range((len(df)//step)+1):
	if i == 678:
		df_steps.append(df.iloc[(i*step):])	
	else:
		df_steps.append(df.iloc[(i*step):((i+1)*step)+1])
means = []
for i in range(len(df_steps)):
	means.append(df_steps[i]['Valore'].mean())
m = pd.DataFrame(means)
m.index = x
m.plot(legend = None)
plt.text(0.25, 0.96,'Max:'+ str(round(m[0].max(),2)), fontsize=10,bbox = dict(facecolor = 'green', alpha = 0.5), transform=plt.gcf().transFigure)
plt.xlabel('time line - 10 min intervals')
plt.ylabel('rain - mm')
plt.title(str(file_clean['Stazione'].loc[file_clean['Stazione'].index[5]])+' ')
plt.ylim(top=22)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
for j in range(14):
	if j != 4 and j != 8 and j != 12:
		plt.axvline(x=j*52560, color = 'orange')
	else:
		plt.axvline(x=j*52704, color = 'orange')
plt.ylim(top=0.3)
plt.savefig('results/'+str(file_clean['Stazione'].loc[file_clean['Stazione'].index[5]])+'.png')