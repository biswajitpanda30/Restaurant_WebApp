import pymongo
from pymongo import MongoClient
from requests import get
from bs4 import BeautifulSoup

urls = []
url = 'https://houseofindia-limbach.de/speisekarte.html'


# Lists to store the scraped data in
names = []
prices = []
ingredients = []
types = []
classes = ["tr", "td"]


#for ittr in range(0, 1):

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
title = html_soup.find_all('title')
dish_container = html_soup.find_all('tr')
dishType = html_soup.find_all('td', {"colspan": "4"})
dishName = html_soup.find_all('td', {"colspan": "2"})
dishDisc = html_soup.find_all('td', {"colspan": "3"})
dishPrice = html_soup.find_all('td', {"class": "right"})
#print(dishDisc)

# Extract data from individual dish container
for i in dishName:
    name = i.text
    names.append(name)
    #print(name)
for i in dishDisc:
    description = i.text
    ingredients.append(description)
    #print(description)
for i in dishPrice:
    price = i.text
    prices.append(price)
    #print(price)

for container in dishType:
    #h2 = container.find_all('h2')
    types = container.find_all('span')

    #print(types)
    j=0
    for  i in types:
        if(j == 0):
            type = i.text
            #print(type)
            types.append(type)
            j=j+1

import json

try:
    conn = MongoClient('mongodb://localhost:27017')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.foodworld

collection = db.dishes


i=0
while i < len(price) :
    food = {'dishName': name[i], 'dishPrice':price[i], 'dishIngredients':description[i], 'type':type}
    i=i+1
    print(json.dumps(food))
    r1 = collection.insert_one(food)
    #
