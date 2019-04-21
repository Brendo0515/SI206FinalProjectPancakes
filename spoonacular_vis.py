import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import json
import unittest

# read data from sql database
def get_recipeTimes(db_filename):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    #extract times it takes to make pancakes in a list
    cur.execute('SELECT timeTo_makeRecipe from Spoonacular')
    recipeTimes = []
    for row in cur:
        recipeTimes += row;
    cur.close()
    # print(recipeTimes)
    return recipeTimes

# get_recipeTimes("pancakes.sqlite")

# calculate the average time it takes to make a pancake
def calc_avg_time (recipeTimes):
    return sum(recipeTimes) / len(recipeTimes)

# print(calc_avg_time(get_recipeTimes("pancakes.sqlite")))

#write calculated data to txt file
file = open('pancakeAvgTime.txt','w')
file.write('The Average Time to Make a Pancake: ')
file.write(str(calc_avg_time(get_recipeTimes("pancakes.sqlite"))))
file.write(' minutes')
file.close()

# plotted the times in a box plot to visualize the data
def plot_times (recipeTimes):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(recipeTimes)
    ax.set_ylabel('Time to Make (min)')
    ax.set_title("Box Plot of Time to Make Pancakes")
    plt.show()

plot_times(get_recipeTimes("pancakes.sqlite"))
