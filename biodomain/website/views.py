from django.shortcuts import render
from website.models import Instruments
from website.models import Institute
from website.models import Category_Description
# Create your views here.


def home(request):
    return render(request,'index.html', {})

def team(request):
    return render(request,'team.html', {})

def InstrumentListpage(request):
    allInst = Instruments.objects.all()
    context={'instruments':allInst}
    return render(request,'instrumentlistpage.html', context)

def InstituteListpage(request):
    allInst = Institute.objects.all()
    context={'institute':allInst}
    return render(request,'institutelistpage.html', context)

def CategoryListpage(request):
    allCategory = Category_Description.objects.all()
    context={'category':allCategory}
    return render(request,'categorylistpage.html',context)

# def multiSearch(request):
#     if request.method == 'POST':
#         category=request.POST.get("category")
#         eqpobj=Equipments.objects.raw('select * from Equipments where category="'+category+'"')
#         return render(request,'listpage.html',{'Equipments':eqpobj})
#     else:
#         eqpobj=Equipments.objects.raw('select * from Equipments')
#         return render(request,'listpage.html',{'Equipments':eqpobj})