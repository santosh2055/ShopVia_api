from django.http import JsonResponse
from bs4 import BeautifulSoup
from requests import get


def index(request):
    # tested using request format like http: // localhost: 8000/polls /?q = hp
    query = request.GET.urlencode()
    url = 'https://www.flipkart.com/search?'+query + \
        '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for a in html_soup.find_all('div',  attrs={'class': '_3liAhj'}):
        name = a.find('a', attrs={'class': '_2cLu-l'})
        price = a.find('div', attrs={'class': '_1vC4OE'})
        rating = a.find('div', attrs={'class': 'hGSR34'})
        result = {"Name": name.text, "Price": price.text,
                  "Rating": ("None" if(rating == None) else rating.text)}
        results.append((result))
    return JsonResponse({'searchResults': results})
