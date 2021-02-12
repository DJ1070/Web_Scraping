import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.zalando.de/damen/?q=Diesel+jeans'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all('div', {'class': 'qMZa55 SQGpu8 iOzucJ JT3_zV DvypSJ'})

filename = 'zalando_diesel_jeans.csv'
f = open(filename, 'w')
headers = 'brand, model, price\n'
f. write(headers)
#print(containers)

for container in containers:
    brand_container = container.findAll('span', {'class': 'u-6V88 ka2E9k uMhVZi FxZV-M uc9Eq5 pVrzNP ZkIJC- r9BRio qXofat EKabf7'})
    brand = brand_container[0].text
    model_container = container.findAll('h3', {'class': 'u-6V88 ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP ZkIJC- r9BRio qXofat EKabf7'})
    model = model_container[0].text
    price_container = container.findAll('span', {'class': 'u-6V88 ka2E9k uMhVZi FxZV-M z-oVg8 pVrzNP cMfkVL'})
    price = price_container[0].text.split()[0]
    f.write(brand + ',' + model + ',' + price + '\n')

f.close()

