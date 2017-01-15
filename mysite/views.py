
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from datetime import datetime
import time
from mysite.models import Product_Category,Product,Blog
from mysite.forms import OrderForm,LoginForm
from twilio.rest import TwilioRestClient
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def sendsms(message):
    account_sid = "AC2cc122cef4e48252b937f91e23eeac64"
    auth_token = "2d6c6b390aec62f2c8c17e49fc9037eb"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to="+2348136823630", from_="+16164389791",
                                     body=message)

def index(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid:
            form.save()
            message=request.POST['Name']+request.POST['PhoneNo']
            sendsms(message)
#     print time
    return render(request,'mysite/home.html',{'form':form})

def Product_table(request):
	products_category=Product_Category.objects.order_by('id')
	return render(request,'mysite/product.html',{'products':products_category})

def login(request):
    form=LoginForm()
    if request.POST:
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            return render(request,'mysite/login_page.html',{'username':request.POST['username']})
        else:
            render(request,'mysite/login.html',{'form':form})
    return render(request,'mysite/login.html',{'form':form})


def investor(request):
	return render(request,'mysite/investor.html')

def Blog_view(request):
    blog=Blog.objects.order_by('id')
    return render(request,'mysite/blog.html',{'blog':blog})
