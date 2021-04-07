from django.http import JsonResponse
from django.http import HttpResponse
from bs4 import BeautifulSoup
from requests import get
def index(request):
    results = []
    query = request.GET.urlencode()[slice(2, len(request.GET.urlencode()), 1)]
#flipkart
    url = 'https://www.flipkart.com/search?q='+query + \
        '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('div',  attrs={'class': '_3liAhj'}):
        link = a.find('a', attrs={'class': 'Zhf2z-'})
        imageLink = None
        name = a.find('a', attrs={'class': '_2cLu-l'})
        price = a.find('div', attrs={'class': '_1vC4OE'})
        rating = a.find('div', attrs={'class': 'hGSR34'})
        result = {"imageLink": ("None" if(imageLink == None) else imageLink.get('src')), "Link": ("None" if(link == None) else 'https://www.flipkart.com'+link.get('href')), "Name": ("None" if(name == None) else name.get('title')), "Price": price.text, }
        results.append((result))

# daraz
    url = 'https://www.daraz.com.np/catalog/?q='+query + \
        '&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.287d2d2bwlEWRd'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('div',  attrs={'class': 'c2prKC'}):
        name = a.find('div', attrs={'class': 'c16H9d'})
        price = a.find('span', attrs={'class': 'c13VH6'})
        # rating = a.find('i', attrs={'class': 'c3dn4k c3EEAg'})
        # halfrating = a.find('i', attrs={'class': 'c3dn4k c3DcGB'})
        result = {"Name": ("None" if(name == None) else name.a.text), "Price": ("None" if(price == None) else price.text),
                  "Rating": "None"}
        results.append((result))

# sastodeal done
    url = 'https://www.sastodeal.com/catalogsearch/result/?q='+query
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    print("Response Response Response Response"+response.text)
    for a in html_soup.find_all('li',  attrs={'class': 'product-item'}):
        link = a.find('a', attrs={'class': 'product-item-photo'})
        imageLink = a.find('img', attrs={'class': 'product-image-photo'})
        name = a.find('strong', attrs={'class': 'product-item-name'})
        price = a.find('span', attrs={'class': 'pricenew'})
        # rating = "null"
        # halfrating = a.find('i', attrs={'class': 'c3dn4k c3DcGB'})
        result = {"imageLink": ("None" if(imageLink == None) else imageLink.get('src')), "Link": ("None" if(link == None) else link.get('href')), "Name": ("None" if(name == None) else name.a.text), "Price": ("None" if(price == None) else price.span.span.span.text),
                  }
        results.append((result))

# nepbay
    url = 'https://market.thulo.com/shopping/search?q='+query
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('div',  attrs={'class': 'ncs-ad-list'}):
        link = a.find('div', attrs={'class': 'TGLBox'})
        imageLink = None
        name = a.find('div', attrs={'class': 'TGLBox'})
        price = a.find('div', attrs={'class': 'TGLBox'})
        # rating = a.find('i', attrs={'class': 'c3dn4k c3EEAg'})
        # halfrating = a.find('i', attrs={'class': 'c3dn4k c3DcGB'})
        result = {"imageLink": ("None" if(imageLink == None) else imageLink.get('src')), "Link": ("None" if(link == None) else link.h4.a.get(
            'href')), "Name": ("None" if(name == None) else name.h4.a.text), "Price": ("None" if(price == None) else price.p.span.text), }
        results.append((result))

# gajabko
    url = 'http://gajabko.com/?s='+query
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('li', attrs={'class': 'product'}):
        link = a.find('a', attrs={'class': 'woocommerce-LoopProduct-link'})
        imageLink = a.find('img', attrs={'class': 'wp-post-image'})
        name = a.find('h3')
        price = a.find('span', attrs={'class': 'price'})
        result = {"imageLink": ("None" if(imageLink == None) else imageLink.get('src')), "Link": ("None" if(link == None) else link.get('href')), "Name": ("None" if(name == None) else name.text), "Price": ("None" if(
            price == None) else price.text)}
        results.append((result))

# socheko
    url = 'https://www.socheko.com/search/'+query
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('li', attrs={'class': 'product-grid-item'}):
        imageLink = a.find('img', attrs={'class': 'ms-img-warpper'})
        link = a.find('a')
        name = a.find('a', attrs={'class': 'product-name'})
        price = a.find('div', attrs={'class': 'price-new'})
        result = {"imageLink": ("None" if(name == None) else imageLink.get('src')), "Link": ("None" if(name == None) else link.get('href')), "Name": ("None" if(name == None) else name.text), "Price": ("None" if(
            price == None) else price.text)}
        print(result)
        results.append((result))

# lds
    url = 'https://lds.com.np/index.php?search='+query + \
        '&category_id=0&submit_search=&route=product%2Fsearch&description=true'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('div', attrs={'class': 'product-block'}):
        imageLink = a.find('img', attrs={'class': 'img-responsive'})
        link = a.find('a', attrs={'class': 'img'})
        name = a.find('div', attrs={'class': 'product-meta'})
        price = a.find('span', attrs={'class': 'price-new'})
        result = {"imageLink": ("None" if(name == None) else imageLink.get('src')), "Link": ("None" if(name == None) else link.get('href')), "Name": ("None" if(name == None) else name.h6.text), "Price": ("None" if(
            price == None) else price.text)}
        results.append((result))

    return JsonResponse({'searchResults': results})
