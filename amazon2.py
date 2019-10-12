import csv #excel file
from urllib.request import urlopen as uReq # web client
from bs4 import BeautifulSoup as soup #data stracture

#url web scrap from www.startech.com.bd
my_url= 'https://www.amazon.com/b?node=16225007011&pf_rd_p=128fe0b0-e107-4f80-9019-5d3120b56a0b&pf_rd_r=3QPD6VB52X6GFGJJRBDN'

#openning up connecting ,grabing the page url
uClient=uReq(my_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup=soup(uClient.read(),"html.parser")
uClient.close()

#grabe each product store page
containers=page_soup.findAll('div',{'class':'s-expand-height'})

container=containers[0]

# name the output file to write to local disk
filename= "Amazon2.csv"

# opens file, and writes headers unicode
f=open(filename,"w",encoding='utf-8')
# header of csv file to be written
headers = ("link, Product_Name, price'\n" )
f.write(headers)

for container in containers:
    link=container.a['href']

    product_container=container.findAll('h2',{'class':'a-size-mini'})
    product_name=product_container[0].text
    
    
    price_container=container.findAll('span',{'class':'a-price-whole'})
    price=price_container[0].text.strip()

    print("link: " +link+ '\n')
    print("product_name: " +product_name+ '\n')
    print("price: " +price+ '\n')

    f.write(link + "," + product_name.replace(",","|") + "," + price +"\n")
f.close()    

    


