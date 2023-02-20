from django.shortcuts import render, redirect, get_object_or_404
from ProfileApp.froms import ProductForm
from ProfileApp.models import Product

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


lstOurProduct = []

def listProduct(request):
    context = {'products': lstOurProduct}
    return render(request, 'ListProduct.html', context)

def InputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            model = form.get('model')
            Case = form.get('Case')
            equipment = form.get('equipment')
            ram = form.get('ram')
            Memory = form.get('Memory')
            SmartWatch = form.get('SmartWatch')
            imember = form.get('imember')

            if model == 'IPone 14':
                iModel = 39800
            elif model == 'IPone 13':
                iModel = 34900
            elif model == 'IPone 12':
                iModel = 29900
            elif model == 'IPone 11':
                iModel = 24900
            else:  #IPone 10
                iModel = 19900

            if Case == 'Limited':
                iCase = 1500
            elif Case == 'Premium':
                iCase = 1000
            elif Case == 'Standard':
                iCase = 800
            else:  # Basic
                iCase = 500

            if equipment == 'AirTag':
                iequipment = 1190
            elif equipment == 'Adepter':
                iequipment = 790
            elif equipment == 'lightning to type c':
                iequipment = 790
            else:  # Adepter USB-C
                iequipment = 790

            if ram == '10':
                iRam = 1900
            elif ram == '8':
                iRam = 1700
            elif ram == '6':
                iRam = 1500
            else:  # 4
                iRam = 1400

            if Memory == '258 GB':
                iMemory = 3000
            elif Memory == '128 GB':
                iMemory = 2000
            else:  # 64 GB
                iMemory = 1500

            if SmartWatch == 'Smartwatch Nike band':
                iSmartwatch = 15900
            elif SmartWatch == 'Smartwatch sport loop midnight':
                iSmartwatch = 15900
            elif SmartWatch == 'Smartwatch Series 8':
                iSmartwatch = 15900
            else:  #SmartWatch Braided Solo Loop
                iSmartwatch = 15900

            isum = iModel + iCase + iequipment + iRam + iMemory + iSmartwatch

            if imember == "Yes":
                discount = isum * 0.10
            else:
                discount = 0

            iTotal = isum - discount

            ProductList = Product(id,model,Case,equipment,ram,Memory,SmartWatch,imember)
            lstOurProduct.append(ProductList)
            return redirect('ListProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form':form}
        return render(request,'InputProduct.html',context)

# def showGoodsList(request):
#     GoodList = Goods.objects.all()
#     context = {'Goods' : GoodList}
#     return render(request,'showGoodsList.html',context)
# def showGoodsOne(request,gid):
#     GoodList = Goods.objects.get(gid=gid)
#     context = {'Goods' : GoodList}
#     return render(request,'showGoodsOne.html',context)
# def newGoods(request):
#     if request.method == 'POST':
#         form = GoodsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS,
#                                  'บันทึกเรียบร้อย')
#             return redirect('showGoodsList')
#         else:
#             Good = Goods.objects.get(gid=request.POST['gid'])
#             if Good:
#                 messages.add_message(request, messages.WARNING,
#                                      'รหัสซ้ำ')
#             else:
#                 messages.add_message(request, messages.WARNING,
#                                      'ข้อมูลไม่ถูกต้อง')
#     else:
#         form = GoodsForm()
#     context = {'form':form}
#     return render(request,'newGoods.html',context)
#
# def updateGoods(request,gid):
#     Good = Goods.objects.get(gid=gid)
#     obj = get_object_or_404(Goods,gid=gid)
#     form = GoodsForm (request.POST or None, instance=obj)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS,'แก้ไขเรียบร้อย')
#             return redirect('showGoodsList')
#         else:
#             messages.add_message(request, messages.WARNING,'ข้อมูลไม่ถูกต้อง')
#     form.GoodsEditForm()
#     context = {'form':form}
#     return render(request, 'updateGoods.html', context)
#
# def deleteGoods(request,gid=None):
#     if request.method == 'POST':
#         gid = request.POST['gid']
#         Good = Goods.objects.get(gid=gid)
#         if Good:
#             Good.delete()
#             messages.add_message(request,messages.SUCCESS,'ลบเรียบร้อย')
#             return  redirect('showGoodsList')
#         else:
#             messages.add_message(request, messages.WARNING,'ไม่พบสินค้า')
#     else:
#         Good = Goods.objects.get(gid=gid)
#         context = {'Goods': Good}
#         return render(request, 'deleteGoods.html', context)