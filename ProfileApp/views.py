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

def myShowData(request):
    ID = '65342310210-9'
    name = 'Panupong Nameyotee'
    Sex = 'ชาย'
    Height = '178'
    weight = '72'
    Food = 'ปลาร้าหมูสับ'
    Color = 'สีแดง'
    domicile = 'อุตรดิตถ์'
    Dream = 'เศรษฐี'
    Pet = 'แมว'
    product = [
        ['OP001', '/static/images/myShowData/figure1.PNG','Luffy gear 4','4500฿'],
        ['OP002', '/static/images/myShowData/figure2.PNG','Roronoa Solo','3500฿'],
        ['OP003', '/static/images/myShowData/figure3.PNG','Luffy - wano kuni','2000฿'],
        ['OP004', '/static/images/myShowData/figure4.PNG', 'Kaido 4 king', '6500฿'],
        ['OP005', '/static/images/myShowData/figure5.PNG', 'shanks 4 king', '5500฿'],
        ['OP006', '/static/images/myShowData/figure6.PNG', 'Doflamingo', '2000฿'],
        ['OP007', '/static/images/myShowData/figure7.PNG', 'Trafalgar D water Law', '4500฿'],
        ['OP008', '/static/images/myShowData/figure8.PNG', 'Edward Newgate', '7000฿'],
        ['OP009', '/static/images/myShowData/figure9.PNG', 'Boa Hancock', '9500฿'],
        ['OP010', '/static/images/myShowData/figure10.PNG', 'Portgas D Ace', '5500฿']
    ]
    context = {'ID':ID,'name':name ,'Sex':Sex,'Height':Height,'weight':weight,'Food':Food
               ,'Color':Color,'domicile':domicile,'Dream':Dream,'Pet':Pet,'product':product}
    return render (request, 'showMyData.html',context)