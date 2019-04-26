# zomato api
import unittest
import sqlite3
import requests
import json
import Zomato_key

#--------------------------------------------
#clear database
#conn = sqlite3.connect("pancakes.sqlite")
#cur = conn.cursor()
#cur.execute("DELETE FROM Zomato")
#conn.commit()
#cur.close()
#--------------------------------------------
key = Zomato_key.key

def add_info(db_filename, res_id, res_name, res_rating):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    #cur.execute('CREATE TABLE IF NOT EXISTS Zomato (Restaurant_ID INTEGER, Restaurant_Name TEXT, Restaurant_Rating INTEGER)')
    cur.execute('INSERT INTO Zomato (Restaurant_ID, Restaurant_Name, Restaurant_Rating) VALUES (?,?,?)', (res_id, res_name,res_rating))
    conn.commit()
    cur.close()

  
count = 0
# repeat search for 20 restaurant ids and names 5 times to get 100 ids/names
for i in range(5):
    #get 20 items
    response = requests.get("https://developers.zomato.com/api/v2.1/search?start="+str(count)+"&count=20&lat=33.7490&lon=-84.3880&radius=50%2C000&cuisines=182",
      headers={"Accept": "application/json", "user-key": key})

    list_of_res_id = json.loads(response.text)["restaurants"]
    for ids in list_of_res_id:
        #add items to database
        res_id = ids["restaurant"]["R"]["res_id"]
        res_name = ids["restaurant"]["name"]
        res_rating = ids["restaurant"]["user_rating"]["aggregate_rating"]
    
        add_info("pancakes.sqlite", res_id, res_name, res_rating)


    #change count to get the next 20 items
    count = count + 20

#fetching the restaurant scores and calculating the average
conn = sqlite3.connect("pancakes.sqlite")
cur = conn.cursor()
cur.execute('SELECT Restaurant_Rating FROM Zomato')
results = cur.fetchall()
total = 0 
for x in results:
  total = total + float(x[0])
average = str(total / 100)


#create txt file
file = open('Zomato_average_rating.txt','w')
file.write('The average rating of breakfast restaurants in Atlanta is ')
file.write(average[0:4])
file.close()
