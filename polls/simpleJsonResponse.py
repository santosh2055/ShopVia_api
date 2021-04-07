# from django.shortcuts import render

# # Create your views here.

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


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
    print(books)
    return JsonResponse({'': books})
