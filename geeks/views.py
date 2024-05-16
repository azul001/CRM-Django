from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,AddRecordForm
from .models import Recode
# Create your views here.


def home(request):
    recodes=Recode.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in. Please try again.")

    return render(request, 'home.html' ,{'recodes':recodes})

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered..! Welcome!!!.")
            return redirect('home')  # Assuming 'home' is the name of your home page URL pattern

    else:
        form = SignUpForm()
        return render(request, 'register_user.html', {'form': form})

    return render(request, 'register_user.html', {'form': form})

@login_required
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Recode.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page.....")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Recode.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Delete Successfully")
        return redirect('home')
    else:
        messages.success(request, "You Must Logged In To Do That....")
        return redirect('home')

@login_required
def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully.")
            return redirect('home')
    else:
        form = AddRecordForm()

    return render(request, 'add_record.html', {'form': form})


@login_required
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Recode.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to do that.")
        return redirect('home')


