
import matplotlib
import sqlite3
import json

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def get_prices(db_filename):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    cur.execute('SELECT price from Yelp')
    prices = []
    for row in cur:
        prices += row
    cur.close()
    #print(prices)
    return prices


num_NA = 0
num_one = 0
num_two = 0
num_three = 0
num_four = 0

for price in get_prices('pancakes.sqlite'):
    if price == 'N/A':
        num_NA += 1
    elif price == '$':
        num_one += 1
    elif price == "$$":
        num_two += 1
    elif price == "$$$":
        num_three += 1
    else: 
        num_four += 1

p = (num_NA, num_one, num_two, num_three, num_four)
#print(p)

ind = np.arange(len(p))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, p, width, color='SkyBlue')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Restaurants in this Price Range')
ax.set_title('Price Ranges of Pancake Restaurants in Atlanta, GA')
ax.set_xticks(ind)
ax.set_xticklabels(('N/A', '\$', '\$\$', '\$\$\$', '\$\$\$\$'))



def autolabel(rects, xpos='center'):
    #"""
    #Attach a text label above each bar in *rects*, displaying its height.

    #*xpos* indicates which side to place the text w.r.t. the center of
    #the bar. It can be one of the following {'center', 'right', 'left'}.
    #"""

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1)


plt.show()

