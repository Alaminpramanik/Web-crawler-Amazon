from urllib.request import urlopen # web client
from bs4 import BeautifulSoup #Beautiful Soup is a  parsing HTML and XML documents.

#url web linkscrap from wwwamazon.com 
html=urlopen("https://www.amazon.com/s/browse?_encoding=UTF8&node=16225009011&ref_=nav_shopall-export_nav_mw_sbd_intl_electronics")

# parses html into a soup data structure to traverse html
bsobj=BeautifulSoup(html.read(), 'lxml')

#for loops over each product and grabs attributes about container
for link in bsobj.findAll('div',{'class':'mainResults'}):
    if 'href' in link.attrs:
        print(link.attrs['href'])

