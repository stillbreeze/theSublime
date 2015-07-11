from django.shortcuts import render
from django.http import Http404, HttpResponse, request

# Create your views here.
def home(request):
	print "AAAAAAAA"
	return render(request,'home.html')