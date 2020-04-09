import sys
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.pyplot import figure
import matplotlib.transforms as mtransforms
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

'''
file_name = str(sys.argv[1])

with open(file_name) as f:
    ts_goal = int(f.readline())
data = pd.read_csv(file_name, skiprows=1, sep=",")
print(ts_goal)

print(data['Service_Time'])
print(data['Time'])
print(data['Degree'])

#sns.set_style("whitegrid")
fig, ax = plt.subplots()
sns.lineplot(x='Time', y='Service_Time', data=data, markers=True, ax=ax)
#data['Service_Time'].max()
#plt.ylim(ymax = 250, ymin = 25)
ax2 = ax.twinx()
sns.lineplot(x='Time', y='Degree', data=data, markers=True, ax=ax2, color='r')
#plt.ylim(ymax = 20, ymin = 0)
ax.axhline(ts_goal, ls='--')
plt.show()
'''

Degree = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256])
Fast_Flow = np.array([100012642, 50010734, 25013117, 12690688, 6320390, 3190800, 1687952, 3344519, 1336063])
Pthread = np.array([91125878, 51236236, 26435453, 13629737, 6693088, 3479733, 1831912, 1799757, 1366533])
sequential = 100003961
ff_1 = 100012642 
pthread_1 = 91125878


fig, ax = plt.subplots()

pthread_speed_up = [sequential / x  for x in Pthread]
ff_speed_up = [sequential / x  for x in Fast_Flow]

ax.set_yscale('log', basey=2)
ax.set_xscale('log', basex=2)
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.grid(linestyle='dashed')
ax.plot(Degree.tolist(), pthread_speed_up,  '-.', marker='*', color='black', label='pthread')
ax.plot(Degree.tolist(), ff_speed_up, '-.', marker='<', color='black', label='fast flow')
ax.plot(Degree.tolist(), Degree.tolist())
ax.set_yticks(Degree.tolist())
plt.gca().set_aspect('equal', adjustable='box')
plt.draw()
ax.set_xticks(Degree.tolist())
plt.legend(loc='upper left')
plt.xlabel('Parallelism Degree')
plt.ylabel('Speed Up')
plt.show()

fig, ax = plt.subplots()
pthread_scalability = [pthread_1 / x  for x in Pthread]
ff_scalability = [ff_1 / x  for x in Fast_Flow]
ax.set_yscale('log', basey=2)
ax.set_xscale('log', basex=2)
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.grid(linestyle='dashed')
ax.plot(Degree.tolist(), pthread_scalability,  '-.', marker='*', color='black', label='pthread')
ax.plot(Degree.tolist(), ff_scalability, '-.', marker='<', color='black', label='fast flow')
ax.plot(Degree.tolist(), Degree.tolist())
ax.set_yticks(Degree.tolist())
plt.gca().set_aspect('equal', adjustable='box')
plt.draw()
ax.set_xticks(Degree.tolist())
plt.legend(loc='upper left')
plt.xlabel('Parallelism Degree')
plt.ylabel('Scalability')
plt.show()

fig, ax = plt.subplots()
pthread_efficiency = [x/y for x, y in zip(pthread_speed_up, Degree.tolist())]#[pthread_1 / x  for x in pthread_speed_up]
ff_efficiency = [x/y  for x,y in zip(ff_speed_up, Degree.tolist())]
print(pthread_efficiency)
ax.set_xscale('log', basex=2)
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.grid(linestyle='dashed')
ax.plot(Degree.tolist(), pthread_efficiency,  '-.', marker='*', color='black', label='pthread_efficiency')
ax.set_xticks(Degree.tolist())
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
ax.plot(Degree.tolist(), ff_efficiency,  '-.', marker='>', color='black', label='ff_efficiency')
plt.ylim(ymax = 1.1, ymin = 0)
plt.legend(loc='lower left')
plt.xlabel('Parallelism Degree')
plt.ylabel('Efficiency')
plt.show()
