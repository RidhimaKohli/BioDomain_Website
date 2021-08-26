from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def listpage(request):
    return render(request,'listpage.html', {})