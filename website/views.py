from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# check if user is logging in
def home(request):
  if request.method == "POST":
    username =request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      messages.success(request, "You have been logged in")
      return redirect('home')
    else:
      messages.success(request, "There was an error please try again")
  return render(request, 'home.html')




def logout_user(request):
  logout(request)
  messages.success(request, "you have been logged out ....")
  return redirect('home')