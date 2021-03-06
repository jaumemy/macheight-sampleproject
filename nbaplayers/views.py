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

        def pairs(arr, n, sum):

            dict_ = dict()
            list_ = []

            for i in range(n):

                temp = sum - arr[i]

                if temp in dict_:
                    count = dict_[temp]

                    for j in range(count):
                        x = (temp, arr[i])
                        list_.append(x)

                if arr[i] in dict_:
                    dict_[arr[i]] += 1

                else:
                    dict_[arr[i]] = 1

            return list_


        arr = []

        for i in response['values']:
            h = int(i['h_in'])
            arr.append(h)

        n = len(arr)

        sum=int(sum)

        result_list = pairs(arr, n, sum)







        context = {
            'response': response,
            'sum': sum,
            'result_list': result_list,
        }

        return render(request, 'player_matches_result.html', context=context)



    context = {
        'response': response,
    }

    return render(request, 'player_matches.html', context=context)
