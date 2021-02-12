import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=processor'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all('div', {'class': 'item-container'})

filename = 'products.csv'
f = open(filename, 'w')
headers = 'brand, product_name, shipping\n'
f. write(headers)
#print(containers)

#img alt="AMD" src="https://
for container in containers:
    #print(container)
    #brand = container.div.div.div.a.img('title')
    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text
    brand = product_name.split()[0]
    shipping_container = container.findAll('li', {'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()

#    f.write(product_name.replace(',', '|') + ',' + shipping + '\n')
    f.write(brand + ',' + product_name.replace(',', '|') + ',' + shipping + '\n')

f.close()