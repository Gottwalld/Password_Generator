import string

from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_UP = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nums = list('0123456789')
    special_chars = list('!?@*')

    lenght = int(request.GET.get('length', 12))

    if request.GET.get('Uppercase') == "on":
        alphabet.extend(alphabet_UP)
    if request.GET.get('Numbers') == "on":
        alphabet.extend(nums)
    if request.GET.get('Special') == "on":
        alphabet.extend(special_chars)

    thepassword = ""
    for i in range(0, lenght):
        thepassword += random.choice(alphabet)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
