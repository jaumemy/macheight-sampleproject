from django.shortcuts import render
import requests
import json

# Create your views here.


def index(request):

    url = 'https://mach-eight.uc.r.appspot.com/'

    response = requests.get(url).json()

    context = {
        'response': response,
    }

    return render(request, 'index.html', context=context)



def player_detail(request):

    url = 'https://mach-eight.uc.r.appspot.com/'

    response = requests.get(url).json()

    context = {
        'response': response,
    }

    return render(request, 'player_detail.html', context=context)



def player_matches(request):

    url = 'https://mach-eight.uc.r.appspot.com/'

    response = requests.get(url).json()

    if request.method == 'POST':

        sum = request.POST.get('sum')

        context = {
            'response': response,
            'sum': sum
        }

        return render(request, 'player_matches_result.html', context=context)



    context = {
        'response': response,
    }

    return render(request, 'player_matches.html', context=context)
