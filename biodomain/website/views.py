from django.shortcuts import render
from website.models import Equipments
# Create your views here.


def home(request):
    return render(request,'index.html', {})



def listpage(request):
    allEquip = Equipments.objects.all()
    context={'equipments':allEquip}
    return render(request,'listpage.html', context)