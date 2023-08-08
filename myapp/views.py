from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid(): 
        form.save()
        username = form.cleaned_data.get('username')
        return redirect('home')
    else:
      form = UserRegisterForm()
      return render(request, 'register.html', {'form': form})

 
def home(request):
  return render(request,'home.html')
  #return HttpResponse("This is homepage")

def about(request):
   return render(request,'about.html')

def contactus(request):
   return render(request,'contactus.html')
