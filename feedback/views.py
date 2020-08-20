from django.shortcuts import render,redirect
from .models import Complain,Suggestion
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home.html')

def add_complain(request):
	if request.method=='POST':
		depart=request.POST['depart']
		complain=request.POST['complain']
		compl=Complain(department=depart,complain=complain)
		compl.save()
		messages.success(request,'Complain has been registered.')
	return render(request,'add-complain.html')

def add_suggestion(request):
	if request.method=='POST':
		depart=request.POST['depart']
		suggestion=request.POST['suggest']
		sugg=Suggestion(department=depart,suggestion=suggestion)
		sugg.save()
		messages.success(request,'Thank you for your suggestion.')
	return render(request,'add-suggestion.html')
