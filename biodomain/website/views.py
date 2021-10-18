from django.shortcuts import render
from website.models import Equipments
# Create your views here.


def home(request):
    return render(request,'index.html', {})



def listpage(request):
    allEquip = Equipments.objects.all()
    context={'equipments':allEquip}
    return render(request,'listpage.html', context)



# def multiSearch(request):
#     if request.method == 'POST':
#         category=request.POST.get("category")
#         eqpobj=Equipments.objects.raw('select * from Equipments where category="'+category+'"')
#         return render(request,'listpage.html',{'Equipments':eqpobj})
#     else:
#         eqpobj=Equipments.objects.raw('select * from Equipments')
#         return render(request,'listpage.html',{'Equipments':eqpobj})