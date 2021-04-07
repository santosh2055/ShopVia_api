from django.http import JsonResponse
from bs4 import BeautifulSoup
from requests import get
import json
query = "laptops"
url = 'https://www.flipkart.com/search?q='+query + \
    '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
results = []
for a in html_soup.find_all('div',  attrs={'class': '_3liAhj'}):
    name = a.find('a', attrs={'class': '_2cLu-l'})
    price = a.find('div', attrs={'class': '_1vC4OE'})
    rating = a.find('div', attrs={'class': 'hGSR34'})
    # print(name.text+"\t"+price.text+"\t" +
    #   ("None" if(rating == None) else rating.text))
    result = '{"Name":'+name.text+', "Price":'+price.text + \
        ', "Rating":'+("None" if(rating == None) else rating.text)+'}'

    # results.append({'\name\': '+name.text+",\n \'price\': "+price.text+"\n \'rating\':" +
    #                 ("None" if(rating == None) else rating.text)})
    results.append(result)
    # products['searchitems'].append('{\"name\":\"'+name.text+'\", \"price\":\"'+price.text+ (",\" rating\":\"null\"" if rating==None else "\", \" rating\":\""+ rating.text+"\"}"))

# print(json.loads(results))
print(results)
data = json.dumps(results, indent=2)
print(data)


def index(request):
    books = [
        {
            'ID': 1,
            'Title': 'Title1',
            'Author': 'Author1',
            'Publisher': 'Publisher1',
            'Year': 'Year1'
        },
        {
            'ID': 1,
            'Title': 'Title1',
            'Author': 'Author1',
            'Publisher': 'Publisher1',
            'Year': 'Year1'
        },
        {
            'ID': 1,
            'Title': 'Title1',
            'Author': 'Author1',
            'Publisher': 'Publisher1',
            'Year': 'Year1'
        },
    ]
    return JsonResponse({'results': books})
