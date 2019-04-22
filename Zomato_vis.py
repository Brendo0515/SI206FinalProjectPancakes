import matplotlib
import matplotlib.pyplot as plt
import sqlite3


# read data from database
conn = sqlite3.connect("pancakes.sqlite")
cur = conn.cursor()

#select all restaurant ratings
cur.execute('SELECT Restaurant_Rating from Zomato')
results = cur.fetchall()
ratings = []
for item in results:
    ratings.append(item[0])
cur.close()
    
# plotted the times in a box plot to visualize the data
fig = plt.figure()
bp = fig.add_subplot(111)
bp.boxplot(ratings)
bp.set_ylabel('Ratings per Restaurant')
bp.set_title("Box Plot of Restaurant Ratings")
plt.show()


