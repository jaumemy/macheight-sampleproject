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



def player_detail(request, pk):

    url = 'https://mach-eight.uc.r.appspot.com/'

    response = requests.get(url).json()

    all_json = pk.replace("'",'"')

    json_dict = json.loads(all_json)

    last_name = json_dict['last_name']
    first_name = json_dict['first_name']
    h_in = json_dict['h_in']
    h_m = json_dict['h_meters']

    list_same_height = []

    for i in response['values']:
        if i['h_in'] == h_in:
            if i['first_name'] == first_name and i['last_name'] == last_name:
                pass
            else:
                list_same_height.append(str(i['last_name']+', '+i['first_name']))


    context = {
        'response': response,
        'all': all,
        'last_name': last_name,
        'first_name': first_name,
        'h_in': h_in,
        'h_m': h_m,
        'list_same_height': list_same_height
    }

    return render(request, 'player_detail.html', context=context)



def player_matches(request):

    url = 'https://mach-eight.uc.r.appspot.com/'

    response = requests.get(url).json()

    if request.method == 'POST':

        sum = request.POST.get('sum')


        def pairs(arr, sum):

            
            pass


        # def pairs(arr, n, sum):
        #
        #     dict_ = dict()
        #     list_ = []
        #
        #     for i in range(n):
        #
        #         number = int(arr[i]['h_in'])
        #         name = arr[i]['last_name']+', '+arr[i]['first_name']
        #
        #         diff = sum - number
        #
        #
        #         if diff in dict_:
        #             count = dict_[diff]
        #
        #             for j in range(count):
        #                 ## I am not sure if next part makes efficiency O(n²). It can be taken out of the function and result will be a list of
        #                 ## elements like this (80, Ŵilliams, John) etc without the first name. That's the best I could come up with
        #
        #                 temp_list = []
        #
        #                 for el in arr:
        #
        #                     if int(el['h_in']) == diff:
        #                         el_name = el['last_name']+', '+el['first_name']
        #                         temp_list.append(el_name)
        #
        #                 ###
        #                 ###
        #                 for ele in temp_list:
        #                     x = (ele, name)
        #                     if x not in list_:
        #                         list_.append(x)
        #                 # x = (el_name, name)
        #                 # list_.append(x)
        #
        #         if number in dict_:
        #             dict_[number] += 1
        #
        #         else:
        #             dict_[number] = 1
        #
        #     return list_
        #
        #
        # arr = []
        #
        # for i in response['values']:
        #     arr.append(i)
        #
        # n = len(arr)
        #
        # sum=int(sum)
        #
        # result_list = pairs(arr, n, sum)
        #
        # if result_list == []:
        #     result_list = ['No players found with this sum']


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
