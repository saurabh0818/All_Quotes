from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from .form import *
from .models import *
import csv


# Create your views here.

# ------------------ admin login ----------------------

def loginpage(request):

    return render(request, 'SuperLogin/login.html/')


def login(request):

    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Autheticate User with Credetial
            user = authenticate(username=username, password=password)
            if user is not None:

                # login with Sepcific User
                auth.login(request, user)
                return redirect('Dashboard')
            else:
                messages.info(request, "Please Enter Valid Credential !!!!")
                return render(request, 'SuperLogin/login.html/')
            messages.info(request, "Login Success!!")
        else:
            messages.info(request, "Please Provide Username And Password Both")

    return render(request, 'SuperLogin/login.html/')

# -------------------- DashBoard Start From Here ------------------------------


def dashboard(request):

    author_data = Author.objects.all().count()
    quotes_total = Quote.objects.all().count()
    special_total = SpecialMessages.objects.all().count()

    lst = {'author_data': author_data, 'quotes_total': quotes_total,
           'special_total': special_total}

    return render(request, 'SuperLogin/dashboard.html/', lst)


# ----------------------- Add Author Manually ---------------------------------

def addauthor(request):

    author_form = AuthorForm()
    auther_data = Author.objects.all()
    if request.method == "POST":
        Author_module = AuthorForm(request.POST)
        if Author_module.is_valid():
            Author_module.save()
            Author_name = request.POST.get('fname')
            messages.success(
                request, " Author  {}  Saved to Database Successfully ✔".format(Author_name))
            return redirect('addauthor')

    lst = {'author_form': author_form, 'auther_data': auther_data}

    return render(request, 'SuperLogin/author.html/', lst)


# ------------------------------ Delete Single Author ---------------------------

def author_delete(request, pk):

    author_data = Author.objects.get(id=pk)

    if request.method == "POST":
        if author_data:
            author_data.delete()
            messages.success(
                request, "Yehhh !!!  Data Deleted Successfully ✔")
            return redirect('addauthor')

    lst = {'author_data': author_data}

    return render(request, 'SuperLogin/author_delete.html/', lst)


# -------------------------------- Update Single Author Data -------------------------

def author_update(request, pk):

    author = Author.objects.get(id=pk)
    author_from = AuthorForm(instance=author)

    if request.method == "POST":
        author_from = AuthorForm(request.POST, instance=author)
        if author_from.is_valid():
            author_from.save()
            messages.success(
                request, "Yehhh !!!  Data Updated Successfully ✔")
            return redirect('addauthor')

    lst = {'author': author_from}

    return render(request, 'SuperLogin/author_update.html/', lst)


# -------------------------------- Add Author name by Files ---------------------------------

def addfileauth(request):
    if request.method == "POST":
        # Exception Handling
        try:

            if request.FILES['csv_file']:
                csv_file = request.FILES['csv_file']
                # Checking File Format
                if not csv_file.name.endswith('.csv'):
                    messages.info(request, 'File is not CSV type')
                    return redirect('addfileauth')
                # Checking File Size
                elif csv_file.multiple_chunks():
                    messages.info(request, "Uploaded file is too big (%.2f MB)." % (
                        csv_file.size/(1000*1000),))
                    return redirect('addfileauth')
                else:
                    # Reading Data from File
                    file_data = csv_file.read().decode("utf-8")
                    lines = file_data.split("\n")
                    lst = []
                    for x in lines:
                        lst.append(x.split(","))

                    # Taking Data one By one from List
                    li = []
                    count = 0
                    try:
                        for onestagelist in lst:
                            if count == len(lst)-1:
                                break
                            else:
                                name = onestagelist[0].replace('\ufeff', '')
                                occupation = onestagelist[1].replace('\r', '')
                                author_insert = Author(
                                    name=name, occupation=occupation)
                                author_insert.save()
                                count += 1
                    except Exception as e:
                        messages.info(request, "Error Occured : {}".format(e))
                        return redirect('addfileauth')

                    else:
                        messages.info(request, "Data Inserted Successfully!!")
                        return redirect('addfileauth')

        except Exception as e:
            print("This is error : {}".format(e))
    return render(request, 'SuperLogin/file.html/')


# ----------------------- Add Quotes Manually ---------------------------------

def addquotes(request):

    quotes_form = QuotesForm()
    quotes_data = Quote.objects.all()
    if request.method == "POST":
        Quotes_module = QuotesForm(request.POST)
        if Quotes_module.is_valid():
            Quotes_module.save()
            Author_name = request.POST.get('Author_Id')
            messages.success(
                request, " Author  {}  Saved to Database Successfully ✔".format(Author_name))
            return redirect('addquotes')

    lst = {'quotes_form': quotes_form, 'quotes_data': quotes_data}

    return render(request, 'SuperLogin/quotes.html/', lst)


# ------------------------------ Delete Single Quotes ---------------------------

def delete_quotes(request, pk):

    quotes_data = Quote.objects.get(id=pk)

    if request.method == "POST":
        if quotes_data:
            quotes_data.delete()
            messages.success(
                request, "Yehhh !!!  Data Deleted Successfully ✔")
            return redirect('addquotes')

    lst = {'quotes_data': quotes_data}

    return render(request, 'SuperLogin/quotes_delete.html/', lst)


# -------------------------------- Update Single Quotes Data -------------------------

def quotes_update(request, pk):

    quotes = Quote.objects.get(id=pk)
    quotes_from = QuotesForm(instance=quotes)

    if request.method == "POST":
        quotes_from = QuotesForm(request.POST, instance=quotes)
        if quotes_from.is_valid():
            quotes_from.save()
            messages.success(
                request, "Yehhh !!!  Data Updated Successfully ✔")
            return redirect('addquotes')

    lst = {'quotes_from': quotes_from}

    return render(request, 'SuperLogin/quotes_update.html/', lst)


# -------------------------------- Add Quotes by Files ---------------------------------

def addfilequote(request):
    if request.method == "POST":
        # Exception Handling
        try:

            if request.FILES['csv_file']:
                csv_file = request.FILES['csv_file']
                # Checking File Format
                if not csv_file.name.endswith('.csv'):
                    messages.info(request, 'File is not CSV type')
                    return redirect('addfileauth')
                # Checking File Size
                elif csv_file.multiple_chunks():
                    messages.info(request, "Uploaded file is too big (%.2f MB)." % (
                        csv_file.size/(1000*1000),))
                    return redirect('addfileauth')
                else:
                    # Reading and Filtering Data from File
                    file_data = csv_file.read().decode("utf-8")
                    lines = file_data.split("\n")
                    lst = []
                    for x in lines:
                        bad_chars = [';', ':', '"', "*"]
                        for i in bad_chars:
                            x = x.replace(i, '')
                        lst.append(x.split(".,"))

                    # Taking Data one By one from List
                    li = []
                    count = 0
                    try:
                        for onestagelist in lst:

                            if count == len(lst)-1:
                                break
                            else:

                                quote = onestagelist[0].replace('\ufeff', '')
                                id_name = onestagelist[1].replace('\r', '')
                                id_name = id_name.split(",")
                                ids = id_name[0]
                                author_instance = Author.objects.get(id=ids)
                                quote = quote.capitalize()
                                types = id_name[1]

                                quotes_insert = Quote(
                                    Author_Id=author_instance, quotes=quote, type_quotes=types)
                                quotes_insert.save()
                                count += 1
                    except Exception as e:
                        messages.info(request, "Error Occured : {}".format(e))
                        return redirect('addquotes')

                    else:
                        messages.info(request, "Data Inserted Successfully!!")
                        return redirect('addquotes')

        except Exception as e:
            print("This is error : {}".format(e))
    return render(request, 'SuperLogin/quotesFile.html/')


# -------------------------------- Add Special Message Type -----------------------

def addcatagories(request):
    catagory = spcl_typeForm()
    cata = spcl_type.objects.all()
    if request.method == "POST":
        print("1st Yes")
        addcata = spcl_typeForm(request.POST, request.FILES)
        if addcata.is_valid():
            addcata.save()
            messages.success(
                request, " Special Message  Saved to Database Successfully ✔")
            return redirect('addcatagories')
    lst = {'catagory': catagory, 'cata': cata}
    return render(request, "SuperLogin/addcatagory.html/", lst)


# ------------------------------ Delete Single Catagory Data ---------------------------

def catagory_delete(request, pk):

    spcl_data = spcl_type.objects.get(id=pk)

    if request.method == "POST":
        if spcl_data:
            spcl_data.delete()
            messages.success(
                request, "Yehhh !!!  Data Deleted Successfully ✔")
            return redirect('addcatagories')

    lst = {'spcl_data': spcl_data}

    return render(request, 'SuperLogin/catagory_delete.html/', lst)


# -------------------------------- Update Catagory Data -------------------------

def catagory_update(request, pk):

    spcltype = spcl_type.objects.get(id=pk)
    spclmsg_from = spcl_typeForm(instance=spcltype)

    if request.method == "POST":
        spclmsg_from = spcl_typeForm(
            request.POST, request.FILES, instance=spcltype)
        if spclmsg_from.is_valid():
            spclmsg_from.save()
            messages.success(
                request, "Yehhh !!!  Data Updated Successfully ✔")
            return redirect('addcatagories')

    lst = {'spclmsg_from': spclmsg_from}

    return render(request, 'SuperLogin/catagory_update.html/', lst)


# -------------------------------- Uplaod Special Messages -------------------------


def specialmsg(request):
    splmsg = SpecialMessageForm()
    spcl_data = SpecialMessages.objects.all()
    if request.method == "POST":
        spclmsg_module = SpecialMessageForm(request.POST)
        if spclmsg_module.is_valid():
            spclmsg_module.save()
            messages.success(
                request, " Special Message  Saved to Database Successfully ✔")
            return redirect('specialmsg')
    lst = {'splmsg': splmsg, 'spcl_data': spcl_data}
    return render(request, "SuperLogin/specialmessage.html/", lst)


# ------------------------------ Delete Single Special Message ---------------------------

def spclmsg_delete(request, pk):

    quotes_data = SpecialMessages.objects.get(id=pk)

    if request.method == "POST":
        if quotes_data:
            quotes_data.delete()
            messages.success(
                request, "Yehhh !!!  Data Deleted Successfully ✔")
            return redirect('specialmsg')

    lst = {'quotes_data': quotes_data}

    return render(request, 'SuperLogin/spclmsg_delete.html/', lst)


# -------------------------------- Update Single Spcial Message Data -------------------------

def spclmsg_update(request, pk):

    spclmsg = SpecialMessages.objects.get(id=pk)
    spclmsg_from = SpecialMessageForm(instance=spclmsg)

    if request.method == "POST":
        spclmsg_from = SpecialMessageForm(request.POST, instance=spclmsg)
        if spclmsg_from.is_valid():
            spclmsg_from.save()
            messages.success(
                request, "Yehhh !!!  Data Updated Successfully ✔")
            return redirect('specialmsg')

    lst = {'spclmsg_from': spclmsg_from}

    return render(request, 'SuperLogin/spclmsg_update.html/', lst)

# -------------------------- User Logout --------------------------------


def logout(request):
    auth.logout(request)
    return render(request, 'SuperLogin/login.html/')
