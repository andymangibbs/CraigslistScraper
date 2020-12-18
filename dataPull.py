import product
import requests
from bs4 import BeautifulSoup


def data_pull():
    keyword = input("Enter your search: ")
    url = 'https://frederick.craigslist.org/search/sss?query=' + keyword + '&sort=rel'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_='result-row')
    online_list = []
    online_final = []
    count = 0

    # populate list with all results
    for result in results:
        date_temp = result.find(class_='result-date')
        info_temp = result.find(class_='result-title hdrlnk')
        price_temp = result.find(class_='result-price')
        link_temp = result.find('a', href=True)
        temp_product = product.Product()
        temp_product.date = date_temp.text
        temp_product.desc = info_temp.text
        temp_product.price = price_temp.text
        temp_product.link = link_temp['href']
        online_list.append(temp_product)
        count = count + 1

    # runs through description of product, if keyword is found, adds to final list
    for i in online_list:
        if keyword.lower() in i.desc.lower():
            online_final.append(i)

    return online_final, keyword
