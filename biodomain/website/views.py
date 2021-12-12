from django.shortcuts import render
from website.models import Instruments
from website.models import Institute
from website.models import Categories
# Create your views here.
import json
from json import dumps

from django.core.mail import send_mail

# def emailForm(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         message = 'You have a mail from ' + name + '\n' + 'Message: ' + message
#         send_mail(subject, message, email, ['bioequipzon@gmail.com'], fail_silently=False)

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:home")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})


def home(request):
    return render(request,'index.html', {})

def team(request):
    return render(request,'team.html', {})

def trial(request):
    return render(request,'trial.html', {})    

def listfrontend(request):
    allInst = Instruments.objects.all()
    context={'instruments':allInst}
    return render(request,'listfrontend.html', context)     

def BasicEquipments(request):
    allInst = Instruments.objects.filter(category='Basic')
    context={'CatInstrument':allInst}
    return render(request,'BasicEquipments.html', context)  

def BioimagingEquipments(request):
    allInst = Instruments.objects.filter(category='Bioimaging')
    context={'CatInstrument':allInst}
    return render(request,'BioimagingEquipments.html', context)          

def CentrifugeEquipments(request):
    allInst = Instruments.objects.filter(category='Centrifuge')
    context={'CatInstrument':allInst}
    return render(request,'CentrifugeEquipments.html',context)  

def CellCultureEquipments(request):
    allInst = Instruments.objects.filter(category='Cell Culture')
    context={'CatInstrument':allInst}
    return render(request,'CellCultureEquipments.html', context)   


def ElectrophoresisEquipments(request):
    allInst = Instruments.objects.filter(category='Electrophoresis')
    context={'CatInstrument':allInst}
    return render(request,'ElectrophoresisEquipments.html',context)  

def ChromatographyEquipments(request):
    allInst = Instruments.objects.filter(category='Chromatography')
    context={'CatInstrument':allInst}
    return render(request,'ChromatographyEquipments.html', context)  

def SpectroscopyEquipments(request):
    allInst = Instruments.objects.filter(category='Spectroscopy')
    context={'CatInstrument':allInst}
    return render(request,'SpectroscopyEquipments.html', context)  

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



def InstrumentView(request):
    allInst = Instruments.objects.all()
    list_of_rows = []
    for row in allInst:
        print("row : ",row)
        # rowdumped = {"iid" : json.dumps(row.iid),"instrumentname":json.dumps(row.instrumentname),"category": json.dumps(row.category) , "instrumentquantity" : json.dumps(row.instrumentquantity) , "instrumentdescription" :json.dumps(row.instrumentdescription),"institute":json.dumps(row.institute),"image": "http://www.sweetwater.com/images/items/120/LPST5HTHDCH-medium.jpg?9782bd"}
        rowdumped = {"iid" : row.iid,"instrumentname":row.instrumentname,"category": row.category , "instrumentquantity" : row.instrumentquantity , "instrumentdescription" :row.instrumentdescription,"institute":row.institute,"image": "http://www.sweetwater.com/images/items/120/LPST5HTHDCH-medium.jpg?9782bd"}
        list_of_rows.append(rowdumped)
        print("----")
    print(list_of_rows)
    context={'instruments':json.dumps(list_of_rows)}
    return render(request,'instrumentlistpage.html',context=context)




def InstituteView(request):
    allInst = Institute.objects.all()
    context={'institute':allInst}
    return render(request,'institutelistpage.html', context)

def CategoryView(request):
    allCategory = Categories.objects.all()
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