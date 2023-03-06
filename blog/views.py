from django.shortcuts import render

# Create your views here.
def home(request):
    author = 'Waxllium Ladrian'
    age = 49
    address = 'The Citadel'
    ctx = {'athr':author, 'age':age, 'addr':address}
    return render(request, 'home.html',context=ctx)