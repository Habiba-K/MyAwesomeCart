from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Product
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from math import ceil

def blog(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}

    return render(request, 'blog/index.html',params)

def contact(request):
     if request.method == 'POST':
          name = request.POST['name']
          email = request.POST['email']
          phone = request.POST['phone']
          content = request.POST['content']
          if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
               messages.error(request, "Please fill the form correctly")
          else:         
               contact= Contact(name=name, email=email, phone=phone, content=content)
               contact.save()
               messages.success(request, "Your message has been successfully sent")
     return render(request, 'blog/contact.html')


def handleSignup(request):
     if request.method == 'POST':
          # get the post parameter
          username = request.POST['username']
          fname = request.POST['fname']
          lname = request.POST['lname']
          email = request.POST['email']
          pass1 = request.POST['pass1']
          pass2 = request.POST['pass2']

          #check your errornous input
          if len(username)>10:
               messages.error(request, "Username must be under 10 characters")
               return redirect('blog')

          if not username.isalnum():
               messages.error(request, "Username should only contain letters and numbers")
               return redirect('blog')  

          if pass1 !=pass1: 
               messages.error(request, "Password do not match")
               return redirect('blog')

          #create the user
          myuser = User.objects.create_user(username, email, pass1)
          myuser.first_name = fname
          myuser.last_name = lname
          myuser.save()
          messages.success(request, "Your account has been successfully created")
          return redirect('blog')
     else:
          return HttpResponse('404 - Not Found')

def handleLogin(request):
      if request.method == 'POST':
          # get the post parameter
          loginusername = request.POST['loginusername']
          loginpassword = request.POST['loginpassword']

          user = authenticate(username= loginusername, password= loginpassword)

          if user is not None:
               login(request, user)
               messages.success(request, "Successfully Logged In")
               return redirect('blog')
          else:    
                messages.error(request, "Invalid Credendials, Please try again")
                return redirect('blog')


def handleLogout(request):
     logout(request)
     messages.success(request, "Successfully Logged Out")
     return redirect('blog')

def productView(request, myid):
     product = Product.objects.filter(id=myid)
   
     return render(request, 'blog/prodView.html', {'product': product[0]})