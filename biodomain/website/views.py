from django.shortcuts import render
from website.models import Instruments
from website.models import Institute
from website.models import Category_Description
# Create your views here.


def home(request):
    return render(request,'index.html', {})

def team(request):
    return render(request,'team.html', {})

def trial(request):
    return render(request,'trial.html', {})    

def BasicEquipments(request):
    return render(request,'BasicEquipments.html', {})  

def BioimagingEquipments(request):
    return render(request,'BioimagingEquipments.html', {})          

def CentrifugeEquipments(request):
    return render(request,'CentrifugeEquipments.html', {})  

def CellCultureEquipments(request):
    return render(request,'CellCultureEquipments.html', {})  

def ElectrophoresisEquipments(request):
    return render(request,'ElectrophoresisEquipments.html', {})  

def ChromatographyEquipments(request):
    return render(request,'ChromatographyEquipments.html', {})  

def SpectroscopyEquipments(request):
    return render(request,'SpectroscopyEquipments.html', {})  

def XrayCrystallographyEquipments(request):
    return render(request,'XrayCrystallographyEquipments.html', {})

def SequencingEquipments(request):
    return render(request,'SequencingEquipments.html', {})  

def PCREquipments(request):
    return render(request,'PCREquipments.html', {})  

def BioreactorEquipments(request):
    return render(request,'BioreactorEquipments.html', {})  

def RefrigeratorEquipments(request):
    return render(request,'RefrigeratorEquipments.html', {})  

def IncubatorEquipments(request):
    return render(request,'IncubatorEquipments.html', {})  

def MiscellaneousEquipments(request):
    return render(request,'MiscellaneousEquipments.html', {})      



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