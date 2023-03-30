from bs4 import BeautifulSoup
import requests
import csv
import json


# Creates CSV
url = "https://www.eater.com/maps/best-restaurants-paris-france"
page_to_scrape = requests.get(url)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

names = soup.findAll(attrs={"class": "c-mapstack__card-hed"})
locations = soup.findAll(attrs={"class": "c-mapstack__address"})
phone = soup.findAll(attrs={'class': 'c-mapstack__phone desktop-only'}, limit=38)

res = open('restaurants.csv', 'w')
writer = csv.writer(res)
paris = open('place.json', 'w')


writer.writerow(['Restaurnt', "Address", "Phone"])

for name, place, call in zip(names, locations, phone):
          writer.writerow([name.h1.text , place.a.text, call.a.text])
res.close()


# Creates JSON 
url = "https://www.eater.com/maps/best-restaurants-paris-france"
page_to_scrape = requests.get(url)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

names = soup.findAll(attrs={"class": "c-mapstack__card-hed"})
locations = soup.findAll(attrs={"class": "c-mapstack__address"})
phone = soup.findAll(attrs={'class': 'c-mapstack__phone desktop-only'}, limit=38)
data = []

for name, place, call in zip(names, locations, phone):
    where = name.h1.text 
    add = place.a.text
    nums  = call.a.text
    
    data.append({
        'Name' : where,
        'Address' : add,
        'Phone' : nums
    })

with open('restaurants.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)