from django import forms
from ProfileApp.models import *

Model_Choice = [('IPone 14', 'IPone 14'),
                ('IPone 13', 'IPone 13'),
                ('IPone 12', 'IPone 12'),
                ('IPone 11', 'IPone 11'),
                ('IPone10', 'IPone10')]

Case_Choice = [('Limited', 'Limited'),
               ('Premium', 'Premium'),
               ('Standard', 'Standard'),
               ('Basic', 'Basic')]

equipment_Choice = [('AirTag', 'AirTag'),
                    ('Adepter', 'Adepter'),
                    ('lightning to type c', 'lightning to type c'),
                    ('Adepter USB-C', 'Adepter USB-C')]

ram_Choice = [('10', '10'),
              ('8', '8'),
              ('6', '6'),
              ('4', '4')]

Memory_Choice = [('258', '258'),
                 ('128', '128'),
                 ('64', '64')]

Smartwatch_Choice = [('Smartwatch Nike band', 'Smartwatch Nike band'),
                     ('Smartwatch sport loop midnight', 'Smartwatch sport loop midnight'),
                     ('Smartwatch Series 8', 'Smartwatch Series 8'),
                     ('Smartwatch Braided Solo Loop', 'Smartwatch Braided Solo Loop')]

imember_Choice = [('Yes', 'Yes'),
                  ('No', 'No'),]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id', 'model', 'Case', 'equipment', 'ram', 'Memory', 'SmartWatch','imember')
        widgets = {
            'id' : forms.TextInput(attrs={'class': 'form-control'}),
            'model' : forms.RadioSelect(attrs={'class': 'form-inline'}, choices=Model_Choice),
            'Case' : forms.RadioSelect(attrs={'class': 'form-inline'}, choices=Case_Choice),
            'equipment':forms.RadioSelect(attrs={'class': 'form-inline'}, choices=equipment_Choice),
            'ram':forms.RadioSelect(attrs={'class': 'form-inline'}, choices=ram_Choice),
            'Memory':forms.RadioSelect(attrs={'class': 'form-inline'}, choices=Memory_Choice),
            'SmartWatch':forms.RadioSelect(attrs={'class': 'form-inline'}, choices=Smartwatch_Choice),
            'imember': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=imember_Choice)
        }

# class GoodsForm(forms.ModelForm):
#             class Meta:
#                 model = Goods
#                 fields = ('GoodsCategory', 'gid', 'name', 'brand', 'model', 'price', 'net', 'property')
#                 widgets = {
#                     'GoodsCategory': forms.Select(attrs={'class': 'form-control'}),
#                     'gid': forms.TextInput(attrs={'class': 'form-control'}),
#                     'name': forms.TextInput(attrs={'class': 'form-control'}),
#                     'brand': forms.TextInput(attrs={'class': 'form-control'}),
#                     'model': forms.TextInput(attrs={'class': 'form-control'}),
#                     'price': forms.NumberInput(attrs={'class': 'form-control'}),
#                     'net': forms.NumberInput(attrs={'class': 'form-control'}),
#                     'property': forms.TextInput(attrs={'class': 'form-control'}),
#                 }
#                 labels = {
#                     'GoodsCategory': 'Category',
#                     'gid': 'ID',
#                     'name': 'Name',
#                     'brand': 'Brand',
#                     'model': 'Model',
#                     'price': 'Price',
#                     'net': 'Net',
#                     'property': 'Property',
#                 }
#
#             def GoodsEditForm(self):
#                 self.fields['gid'].widget.attrs['readonly'] = True
#                 self.fields['gid'].labels = 'ID (Not Allowes To Edit)'
#
# Gender_Choice = [('Male','Male'), ('Female','Female')]
#
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ('cid', 'name', 'surname', 'password', 'address', 'telephone', 'gender', 'carreer')
#         widgets = {
#             'cid': forms.TextInput(attrs={'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'surname': forms.TextInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'telephone': forms.TextInput(attrs={'class': 'form-control'}),
#             'Gender': forms.RadioSelect(attrs={'class': 'form-inline'}, choices= Gender_Choice),
#             'carreer': forms.TextInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'cid': 'ID',
#             'name': 'Name',
#             'surname': 'Surname',
#             'password': 'Password',
#             'telephone': 'Telephone',
#             'gender': 'Gender',
#             'carreer': 'Carreer',
#         }
#
#     def CustomerEditForm(self):
#         self.fields['cid'].widget.attrs['readonly'] = True
#         self.fields['cid'].labels = 'ID (Not Allowed To Edit)'