from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def category(request):
    return render(request,"category.html")

def about(request):
    return render(request,"about.html")

def post(request):
    return render(request,"post.html")