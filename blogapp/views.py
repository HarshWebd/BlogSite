from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.

# Fetching blog post from the table
def ShowBlog(request):
    posts_per_page = 1
    udata = BlogPost.objects.all()
    paginator = Paginator(udata,posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'app/blog.html',{'key':page_obj})


# Home Page View
def ShowHome(request):
    return render(request,'app/home.html',{})

# Contact Page View
def ShowContact(request):
    return render(request,'app/contact.html',{})

# About Page View
def ShowAbout(request):
    return render(request,'app/about.html',{})

# Insert Data View
def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    message = request.POST['message']

    usr = User.objects.create(Firstname = fname, Lastname = lname, Email = email, Contact = contact, Message = message)

    # open home page
    return render(request, 'app/home.html',{})