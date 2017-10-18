from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'placeholder to later display all the list of blog'
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display new form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, blog_number):
    message = 'placeholder to display blog ' + blog_number
    return HttpResponse(message)

def edit(request, blog_number):
    message = 'placeholder to edit blog ' + blog_number
    return HttpResponse(message)

def destroy(request, blog_number):
    return redirect('/blogs')