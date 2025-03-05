from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

def home(request):

    records = Record.objects.all()

    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged In ...")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_id = Record.objects.get(id=pk)
        delete_id.delete()
        messages.success(request, "Record Deletes Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must be logged in to do that...")
        return render(request, 'home.html')