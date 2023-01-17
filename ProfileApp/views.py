from django.shortcuts import render, HttpResponse

# Create your views here.
def base(request):
    return render(request, 'base.html')
def Menu(request):
    return render(request, 'Menu.html')
def Home(request):
    return render(request, 'Home.html')
def Header(request):
    return render(request, 'Header.html')
def Profile(request):
    return render(request, 'Profile.html')
def Education(request):
    return render(request, 'Education.html')
def interests(request):
    return render(request, 'interests.html')
def Sale(request):
    return render(request, 'Sale.html')
def Idol(request):
    return render(request, 'Idol.html')
def Contact(request):
    return render(request, 'Contact.html')