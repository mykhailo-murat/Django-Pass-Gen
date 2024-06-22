from django.shortcuts import render
import random


# from django.http import HttpResp

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    thepass = ''

    length = int(request.GET.get('length', 15))
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('specials'):
        characters.extend(list('!@#$%^&*_+'))

    for x in range(length):
        thepass += random.choice(characters)

    return render(request, 'generator/password.html', {'thepass': thepass})

def description(request):
    return render(request, 'generator/description.html')
