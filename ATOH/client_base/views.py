from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_users(request):
    return HttpResponse("Users got")

def get_sorted_users(request):
    return HttpResponse("Users sorted got")