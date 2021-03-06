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

                number = int(arr[i]['h_in'])
                name = arr[i]['last_name']+', '+arr[i]['first_name']

                diff = sum - number

                if diff in dict_:
                    count = dict_[diff]

                    for j in range(count):
                        x = (diff, name)
                        list_.append(x)

                if number in dict_:
                    dict_[number] += 1

                else:
                    dict_[number] = 1

            return list_


        arr = []

        for i in response['values']:
            arr.append(i)

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
