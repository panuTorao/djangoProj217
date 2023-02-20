from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=6 ,default='' ,primary_key=True)
    model = models.CharField(max_length=100 ,default='')
    Case = models.CharField(max_length=100, default='')
    equipment = models.CharField(max_length=100, default='')
    ram = models.CharField(max_length=20, default='')
    Memory = models.CharField(max_length=50, default='')
    SmartWatch = models.CharField(max_length=50, default='')
    imember = models.CharField(max_length=50,default='')

    def iModel(self):
        if self.model == 'IPone 14 ':
            iModel = 39800
        elif self.model == 'IPone 13 ':
            iModel = 34900
        elif self.model == 'IPone 12':
            iModel = 29900
        elif self.model == 'IPone 11 ':
            iModel = 24900
        else:#IPone10
            iModel = 19900
        return iModel

    def iCase(self):
        if self.Case == 'Limited':
            iCase = 1500
        elif self.Case == 'Premium':
            iCase = 1000
        elif self.Case == 'Standard':
            iCase = 800
        else: #Basic
            iCase = 500
        return iCase

    def iequipment(self):
        if self.equipment == 'AirTag':
            iequipment = 1190
        elif self.equipment == 'Adepter':
            iequipment = 790
        elif self.equipment == 'lightning to type c':
            iequipment = 790
        else: #Adepter USB-C
            iequipment = 790
        return iequipment

    def iRam(self):
        if self.ram == '10':
            iRam = 1900
        elif self.ram == '8':
            iRam = 1700
        elif self.ram == '6':
            iRam = 1500
        else: #4
            iRam = 1400
        return iRam
    def iMemory(self):
        if self.Memory == '258 GB':
            iMemory = 3000
        elif self.Memory == '128 GB':
            iMemory = 2000
        else: #64 GB
            iMemory = 1500
        return iMemory
    def iSmartwatch(self):
        if self.SmartWatch == 'Smartwatch Nike band':
            iSmartwatch = 15900
        elif self.SmartWatch == 'Smartwatch sport loop midnight':
            iSmartwatch = 15900
        elif self.SmartWatch == 'Smartwatch Series 8':
            iSmartwatch = 15900
        else:#Smartwatch Braided Solo Loop
            iSmartwatch = 15900
        return iSmartwatch

    def isum (self):
        isum = self.iModel() + self.iCase() + self.iequipment() + self.iRam() + \
               self.iMemory() + self.iSmartwatch()
        return isum

    def idiscount(self):
        if self.imember == "Yes":
            idiscount = self.isum() * 0.10
        else:
            idiscount = 0
        return idiscount

    def iTotal(self):
        iTotal = self.isum() - self.idiscount()
        return iTotal


# class GoodsCategory(models.Model):
#     gc_name = models.CharField(max_length=100, default='')
#     desc = models.CharField(max_length=200 , default='')
#
#     def __str__(self):
#         return  str(self.id) + ' : ' + str(self.gc_name)
#
# class Goods(models.Model):
#     GoodsCategory = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE,default=None)
#     gid = models.CharField(max_length=100, default='',primary_key=True)
#     name = models.CharField(max_length=100 , default='')
#     brand = models.CharField(max_length=100, default='')
#     model = models.CharField(max_length=100, default='')
#     price = models.FloatField(default=0.00)
#     net = models.IntegerField(default=0)
#     property = models.CharField(max_length=1000, default='')
#
#     def __str__(self):
#         return str(self.gid) + ' : ' + str(self.name)
# class Customer(models.Model):
#     cid = models.CharField(max_length=100, default='', primary_key=True)
#     name = models.CharField(max_length=100 , default='')
#     surname = models.CharField(max_length=100, default='')
#     address = models.CharField(max_length=100, default='')
#     telephone = models.CharField(max_length=100, default='')
#     gender = models.CharField(max_length=100, default='')
#     carreer = models.CharField(max_length=100, default='')
#     password = models.CharField(max_length=100, default='')
#
#     def __str__(self):
#         return str(self.cid)
#
# class Order(models.Model):
#     oid = models.CharField(max_length=100, default='', primary_key=True)
#     dete = models.CharField(max_length=100, default='')
#     customer = models.CharField(max_length=100, default='')
#     status = models.CharField(max_length=100, default='')
#
#     def __str__(self):
#         return str(self.oid)
#
# class OrderDetail(models.Model):
#     order = models.CharField(max_length=100 , default='')
#     goods = models.CharField(max_length=100 , default='')
#     price = models.FloatField(default=0.00)
#     quantity = models.IntegerField(default=0)
#     def __str__(self):
#         return  str(self.id)

