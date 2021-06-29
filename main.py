import requests
from bs4 import BeautifulSoup
import pandas as pd

useragent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

#Send get() request and fetch webpage contents
response = requests.get('https://www.amazon.de/s?i=electronics&bbn=3468301&rh=n%3A562066%2Cn%3A%21569604%2Cn%3A1384526031%2Cn%3A3468301%2Cp_36%3A0-20000&pf_rd_i=571954&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_p=a48ddaf6-7e9a-491c-83b4-d51140e9348f&pf_rd_p=a48ddaf6-7e9a-491c-83b4-d51140e9348f&pf_rd_r=SH7ZW76V3WDTCAEMH6SP&pf_rd_r=SH7ZW76V3WDTCAEMH6SP&pf_rd_s=merchandised-search-leftnav&pf_rd_t=101&ref=amb_link_3', headers=useragent)
webpage = response.content


#check status code (optional)
#print(response.status_code)


#create beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")




namelist = []
pricelist = []

for parent in soup.find_all('div', attrs={'class':'a-section a-spacing-medium'}):   #parent element

    #find names and prices
    name = parent.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
    price = parent.find('span', attrs={'class':'a-price-whole'})
    

    #append to lists, check if existent
    if name is not None:
        namelist.append(name.text.strip()[:50])
    else:
        namelist.append("Unknown Product Name")

    if price is not None:
        pricelist.append(price.text.strip())
    else:
        pricelist.append("Unknown Price")


#create dataframe  
df = pd.DataFrame({
    'Title': namelist,
    'Price': pricelist
}, columns=['Title', 'Price'])


#create csv file
df.to_csv('amazon_smartphone_comparison.csv', index=False, header=True)

print(df)