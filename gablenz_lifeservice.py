import pymongo
from pymongo import MongoClient
from requests import get
from bs4 import BeautifulSoup

urls = []
urls.append('https://www.gablenz-eck-lieferservice.de/speisekarte-salate')
urls.append('https://www.gablenz-eck-lieferservice.de/speisekarte-pizza')
#urls.append('https://www.gablenz-eck-lieferservice.de/speisekarte-pasta')

# Lists to store the scraped data in
names = []
prices = []
ingredients = []
types = []
classes = ["tr", "td", "span"]


for temp in range(0, 2):

    response = get(urls[temp])

    html_response = BeautifulSoup(response.text, 'html.parser')
    title = html_response.find_all('title')
    dish_container = html_response.find_all('tr', class_ = 'article_bgcolorb')
    dishType = html_response.find("meta", itemprop= "name")

    # Extract data from individual dish container
    for container in dish_container:
        span = container.find_all('span', class_ = 'article_name')
        span1 = container.find_all('span', class_ = 'description')
        td = container.find_all('td', class_ = 'prbox_bg_1 price_td_1')
        j=0
        for  i in span:
            if(j == 0):
                name = i.text
                names.append(name)
                j=j+1
        i=0
        for  j in span1:
            if(i == 0):
                description = j.text
                ingredients.append(description)
                i=i+1
        for row in td:
            meta = row.find_all('meta')
            title = row.find("meta", itemprop="price")
            prices.append(title["content"])
        types.append(dishType["content"])

response = get(urls[0])
html_response = BeautifulSoup(response.text, 'html.parser')

restaurant_details = html_response.find('span', {"class" : "displaynot_mobile"})
restaurant = restaurant_details.text
restaurant = restaurant.replace('\u2002', ' ')


import json

try:
    dbconnection = MongoClient('mongodb://localhost:27017')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = dbconnection.foodie

collection = db.menu


i=0
while i < len(prices) :
    dishes_menu = {'cuisineName': names[i], 'cuisineIngredients':ingredients[i], 'cuisineType':types[i], 'cuisinePrice':prices[i],'restaurantDetails':restaurant}
    i=i+1
    print(json.dumps(dishes_menu))
    data = collection.insert_one(dishes_menu)
    #
