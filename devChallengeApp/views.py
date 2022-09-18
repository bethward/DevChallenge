from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.
def indexPageView (request) :
    return render(request, 'devChallengeApp/index.html')

# def howPageView (request) :
#     return HTTPResponse('This is the how')  