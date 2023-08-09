from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from .models import ContactMessage
from django.core.mail import send_mail
from .models import Upload

from django.shortcuts import render
from .models import ContactMessage, Upload

def display_data(request):
    contact_messages = ContactMessage.objects.all()
    uploads = Upload.objects.all()
    return render(request, 'display_data.html', {'contact_messages': contact_messages, 'uploads': uploads})
 
def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        # Process the CSV file and save data to the database
        for line in csv_file:
            # Parse the CSV data and create Book objects
            title, author = line.decode().strip().split(',')
            Upload.objects.create(title=title, author=author)
        return redirect('upload_success')
    return render(request, 'upload_form.html')

def upload_success(request):
    return render(request, 'upload_success.html')

def contactus(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
             name = form.cleaned_data['name']
             email = form.cleaned_data['email']
             message = form.cleaned_data['message']
             
             contact_message = ContactMessage.objects.create(name=name,email=email, message=message)
             
             send_mail(subject='testing django',
                       message =f'Name: {name}\nEmail: {email}\nMessage: {message}',
                       from_email='rajandeepkaur446@gmail.com',
                       recipient_list=['rajandeepkaur61@outlook.com'])
             return redirect('contactus')

    return render(request, 'contactus.html', {'form': form})
def register(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid(): 
        form.save()
        username = form.cleaned_data.get('username')
        return redirect('home')
    else:
      form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

 
def home(request):
  return render(request,'home.html')
  #return HttpResponse("This is homepage")

def about(request):
   return render(request,'about.html')

# def contactus(request):
#    return render(request,'contactus.html')
