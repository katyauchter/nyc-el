from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    """The home page"""
        
    return render(request, 'home.html')

def link1(request):
	"""A New Page #1"""
	
	return render(request, 'link1.html')
	
def link2(request):
	"""A New Page #2"""
	
	return render(request, 'link2.html')

def link3(request):
	"""A New Page #3"""
	
	return render(request, 'link3.html')
	
