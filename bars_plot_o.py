# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:13:00 2015

@author: kqo
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

## the data

f = open('areas.txt', 'r') 
lines = f.readlines()[1:5]
f.close() 

c1s = [] #initiate the lists containing the data
o1s = [] #initiate the lists containing the data
name = []

for line in lines:
    p = line.split() #split every line in lines 
    c1s.append(float(p[1])) #append each line of column 1
    o1s.append(float(p[2])) #append each line of column 2
    name.append(p[0]) #creates naming of axis

N = int(len(c1s))

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.25                      # the width of the bars
space = 0.25

## the bars
bar1 = ax.bar(ind, c1s, width,
                color='green')

bar2 = ax.bar(ind+space, o1s, width,
                    color='red')

# axes and labels
ax.set_xlim(-width,len(ind))
ax.set_ylim(0,9)
ax.set_ylabel('Normalised intensity')
ax.set_title('Emissions normalised to In3d3/2 or Si2p3/2')
xTickMarks = name #['Group'+str(i) for i in range(1,8)]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)
#ax.spines["top"].set_visible(False)  
#ax.spines["right"].set_visible(False)  

## add a legend
ax.legend( (bar1[0], bar2[0]), ('C1s', 'O1s') )

plt.savefig("areas.png", dpi = 200)
plt.show()