import csv #excel file
from urllib.request import urlopen as uReq # web client
from bs4 import BeautifulSoup as soup #data stracture

#url web scrap from www.startech.com.bd
my_url= 'https://www.cookcountyassessor.com/Property.aspx?mode=details&pin=16353000090000'

#openning up connecting ,grabing the page url
uClient=uReq(my_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(),"html.parser")
uClient.close()

#find the element of page store
containers=page_soup.findAll('div', {'class':'characteristics'})

#loops over each product and grabs attributes about
container=containers[0]

# name the output file to write to local disk
filename= "cookcountyassessor.csv"

# opens file, and writes headers unicode
f=open(filename,"w",encoding='utf-8')
# header of csv file to be written
headers = ("Pin, property_location, city '\n' " )
f.write(headers)

#for loops over each product and grabs attributes about container
for container in containers:

    pin_container=container.findAll('span',{'id':'ctl00_phArticle_ctlPropertyDetails_lblPropInfoPIN'})
    pin=pin_container[0].text

    property_location_container=container.findAll('span',{'id':'ctl00_phArticle_ctlPropertyDetails_lblPropInfoAddress'})
    property_location=property_location_container[0].text

    city_container=container.findAll('span',{'id':'ctl00_phArticle_ctlPropertyDetails_lblPropInfoCity'})
    city=city_container[0].text

    print("pin: " + pin +"\n")
    print("property_location: " + property_location + "\n")
    print("city: " + city + "\n")

    f.write(pin + "," + property_location.replace(",","|") + city + "\n")
f.close()


