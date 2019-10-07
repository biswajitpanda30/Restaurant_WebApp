import pymongo
from pymongo import MongoClient
from requests import get
from bs4 import BeautifulSoup

urls = []
urls.append('http://www.littleindia-dresden.de/menu/vegetarsiche-gerichte')
urls.append('http://www.littleindia-dresden.de/menu/dessert')
urls.append('http://www.littleindia-dresden.de/menu/vorspeise')
#url = 'http://www.littleindia-dresden.de/menu/vegetarsiche-gerichte'
#url = 'http://www.littleindia-dresden.de/menu/dessert'
#url = 'http://www.littleindia-dresden.de/menu/vorspeise'

# Lists to store the scraped data in
names = []
prices = []
ingredients = []
types = []
classes = ["td", "span", "em"]


for ittr in range(0, 3):

    response = get(urls[ittr])

    html_soup = BeautifulSoup(response.text, 'html.parser')

    dish_container = html_soup.find_all('tr', class_ = 'seznam')

    dishType = html_soup.find('h2', class_ = 'title')

    print("Hello")
    print(ittr)
    # Extract data from individual dish container
    for container in dish_container:
        td = container.find_all('td')
        j=0
        for  i in td:
            if(j == 0):
                j=j+1
            else :
                if(j == 1):
                    name = i.text
                    names.append(name)
                    j=j+1
                    types.append(dishType)

                else:
                    if(j == 2):
                        price = i.text
                        price = price.replace('\u20ac', '')
                        price = price.replace('\r\n', '')
                        #price = price.replace('\xa0\xa0\xa010.29 \xa0\xa0\xa0', '')
                        price = price.strip()
                        prices.append(price)
                        j=j+1



    tr = html_soup.find_all('tr')
    for row in tr:
        td = row.find_all(classes[ittr] , class_ = 'style4')
        for i in td:
            ingradient = i.text
            ingradient = ingradient.replace(u'\u00dfe', '')
            ingradient = ingradient.replace(u'K\u00e4se', '')
            ingradient = ingradient.replace(u'K\u00fcche', '')
            ingradient = ingradient.replace('\n', '')
            ingradient = ingradient.replace('\r\n', '')
            ingredients.append(ingradient)



response = get(urls[0])
html_soup = BeautifulSoup(response.text, 'html.parser')

rdetails = html_soup.find('div', {"id" : "copyright"})
restaurantDetails = rdetails.text
restaurantDetails = restaurantDetails.replace('\r\n\n', '')
restaurantDetails = restaurantDetails.replace('\r\n', '')
restaurantDetails = rdetails.text[26:]
restaurantName = restaurantDetails[:12]
restaurantAddress = restaurantDetails[23:52]
restaurantEmail = restaurantDetails[55:82]
restaurantPhone = restaurantDetails[90:102]

import json

try:
    conn = MongoClient('mongodb://localhost:27017')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.foodworld

collection = db.dishes


i=0
while i < len(ingredients) :
    food = {'dishName': names[i], 'dishPrice':prices[i], 'dishIngredients':ingredients[i],'type':types[i+10], 'restaurantName':restaurantName, 'restaurantAddress':restaurantAddress,'restaurantEmail':restaurantEmail,'restaurantPhone':restaurantPhone}
    i=i+1
    print(json.dumps(food))
    r1 = collection.insert_one(food)
    #
