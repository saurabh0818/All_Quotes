from typing import Counter
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from SuperLogin.models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):

    # Create and Append Alphabate A to Z into list
    test_list = []
    alpha = 'a'
    for i in range(0, 26):
        test_list.append(alpha)
        alpha = chr(ord(alpha) + 1)

    # Checking Alphabate Start from A to Z into Author Database
    Alpha = []
    for x in test_list:
        auth = Author.objects.filter(name__startswith=x)
        if auth:
            Alpha.append(x)

    # Checking Catagory into Quotes
    cata = Quote.objects.order_by().values('type_quotes').distinct()
    catago = list(ab['type_quotes'] for ab in cata)

    # Checking Catagory of Special Message
    spcl_cata = spcl_type.objects.order_by().values('catagories').distinct()
    spcl_catago = list(new_list['catagories'] for new_list in spcl_cata)

    # Finding Any 1000 Data from Database
    models_less_than_seventy = []
    Models_less_then_Thirty_Five = []
    mymodel = Quote.objects.all().order_by('?')[:1000]

    # Checking Quotes Less Then 70 Words and Greater Then 65 Words.
    for single_data in mymodel:
        if len(single_data.quotes) <= 70 and len(single_data.quotes) >= 65:
            models_less_than_seventy.append(
                {'author': single_data.Author_Id.name, 'quotes': single_data.quotes})

    # Checking Length of Quotes Under 65 to 75
    Total_length_of_Quotes = len(models_less_than_seventy)
    # importing Random Package

    import random
    random_number_for_quotes = random.randint(1, Total_length_of_Quotes-1)

    Seventy_five_character_quotes = models_less_than_seventy[random_number_for_quotes]

    # Checking Quotes Less Then 38 Words and Greater Then 20 Words.
    for single_data in mymodel:
        if len(single_data.quotes) <= 38 and len(single_data.quotes) >= 10:
            Models_less_then_Thirty_Five.append(
                {'author': single_data.Author_Id.name, 'quotes': single_data.quotes})

    # Checking Length of Quotes Under 38 to 20
    Total_length_of_Quotes_Small = len(Models_less_then_Thirty_Five)

    # Generate Random Number for Small Quotes
    random_number_for_quotes_small = random.randint(
        1, Total_length_of_Quotes_Small-1)

    Thirty_five_character_quotes = Models_less_then_Thirty_Five[random_number_for_quotes_small]

    # Top Three Special Type Messages
    special_data = spcl_type.objects.all()
    sett = set()  # creating set
    # import random number package
    import random
    try:
        while True:

            if len(sett) == 3:
                break
            else:
                sett.add(random.randint(0, len(special_data) - 1))

    except:
        pass

    # Appending Three Special Type Data from All
    special_datas = []
    for x in sett:

        special_datas.append(special_data[x])

    # Database count for User

    total_data_author = Author.objects.all().count()
    total_data_quotes = Quote.objects.all().count()
    total_data_spcl_msgs = SpecialMessages.objects.all().count()

    # List of Data Send to the Templates.
    lst = {'Alpha': Alpha,
           'catago': catago[0:15], 'spcl_catago': spcl_catago[0:15], 'seventy_five_char_word': Seventy_five_character_quotes, 'thirty_five_char_word': Thirty_five_character_quotes, 'special_data': special_datas, 'total_data_author': total_data_author, 'total_data_quotes': total_data_quotes, 'total_data_spcl_msg': total_data_spcl_msgs}
    return render(request, "frontend/index.html/", lst)


# Search all Author

def Authors(request):

    authors = Author.objects.all()
    total_auth = Author.objects.all().count()

    dic = {'Auth': authors, 'total': total_auth}

    return render(request, "frontend/Author.html/", dic)


# search author by first letter

def Authorss(request, data):

    if data == None or data == "":
        pass
    else:
        authors = Author.objects.all().filter(name__startswith=data)

    start_wit = data.upper()

    dicto = {'authors': authors, 'start_wit': start_wit}

    return render(request, "frontend/Authors.html/", dicto)

# Wishes Function


def wishes(request):

    total_spcl_messages = spcl_type.objects.all()
    paginator = Paginator(total_spcl_messages, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    spcl_dic = {'total_spcl_messages': page_obj, }
    return render(request, 'frontend/wishes.html/', spcl_dic)


# Quotes Catagories

def Catagories(request):

    # Checking Catagory into Quotes
    cata = Quote.objects.order_by().values('type_quotes').distinct()
    catago = list(ab['type_quotes'] for ab in cata)

    dic = {'catago': catago}
    return render(request, 'frontend/Catagories.html/', dic)

# Special Days function


def Special_days(request):

    # Checking Catagory into Quotes
    days = special_data = spcl_type.objects.all()

    dic = {'days': days}
    return render(request, 'frontend/days_catagory.html/', dic)


def Quotes(request, name):

    if name == None or name == "":
        pass
    else:
        auth_name = Author.objects.get(name=name)
        auth_quotes = Quote.objects.filter(Author_Id=auth_name)

        lst_details = [auth_name, auth_name.occupation]
        lst_quotes = []
        for x in auth_quotes:
            lst_quotes.append(x.quotes)

        paginator = Paginator(lst_quotes, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    dic = {'lst_details': lst_details, 'lst_quotes': page_obj}
    return render(request, 'frontend/Quotes.html/', dic)


# Function for Quotes filter by Catagories

def Catagory(request, type):

    data = Quote.objects.filter(type_quotes=type)

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    types = type
    dic = {'data': page_obj, 'types': types}
    return render(request, 'frontend/Catagory.html/', dic)


# Function to find Days Quotes

def Days(request, day):
    if day:
        spcl_day = SpecialMessages.objects.filter(quotes_type__catagories=day)
        paginator = Paginator(spcl_day, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        dic = {'spcl_day': page_obj}
    else:
        pass

    return render(request, 'frontend/Days.html/', dic)


def BirthDay(request, type):
    if type:
        all_day = SpecialMessages.objects.order_by().values('sub_type').distinct()
        spcl_day = SpecialMessages.objects.filter(
            quotes_type__catagories="Birth Day", sub_type=type)
        paginator = Paginator(spcl_day, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        dic = {'spcl_day': page_obj, 'all_day': all_day}
    else:
        pass

    return render(request, 'frontend/birthday.html/', dic)
