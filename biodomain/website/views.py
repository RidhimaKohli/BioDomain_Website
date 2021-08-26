from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html', {})

def listpage(request):
    return render(request,'listpage.html', {})