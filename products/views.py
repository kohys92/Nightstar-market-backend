import json
import csv

from datetime import datetime
from django import views

from django.views import View
from django.http import JsonResponse

from .models import Menu, MainCategory, SubCategory, Product, ProductImage, Allergy 

class ProductViewer(View):
    def post(self, request):
        try:            
            data          = json.loads(request.body) 
            menu          = Menu.objects.create(name = data['menu'])
            main_category = MainCategory.objects.create(name= data['main_category'], menu = menu)
            sub_category  = SubCategory.objects.create(name = data['sub_category'], main_category = main_category)
            product       = Product.objects.create(
                name          = data['name'],
                sub_category  = sub_category, 
                price         = data['price'],
                discount      = data['discount'],
                sales_unit    = data['sales_unit'],
                weight        = data['weight'],
                shipping_type = data['shipping_type'],
                origin        = data['origin'],
                package_type  = data['package_type'],
                infomation    = data['infomation'],
                created_at    = ''.replace(microsecond = 0),
                updated_at    = ''.replace(microsecond = 0),
                )
            
            ProductImage.objects.create(
                image_url = data['image_url'],
                product   = product,
            )        
            
            Allergy.objects.create(
                name    = data['allergy'],
                product = product,
            )
            
            return JsonResponse({'message' : 'CREATED'}, status = 201)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        
    def get(self,request):
        try:
            products = Product.objects.all()
            return JsonResponse({'results' : [
                {
                    'name'          : product.name,
                    'price'         : product.price,
                    'discount'      : product.discount,
                    'sales_unit'    : product.sales_unit,
                    'weight'        : product.weight,
                    'shipping_type' : product.shipping_type,
                    'origin'        : product.origin,
                    'package_type'  : product.package_type,
                    'infomation'    : product.infomation,
                    'created_at'    : product.created_at,
                    'updated_at'    : product.updated_at,
                    'sub_category'  : product.sub_category.name,
                    'main_category' : product.sub_category.main_category.name,
                    'menu'          : product.sub_category.main_category.menu.name,
                    'image_list'    : [img.image_url for img in product.productimage_set.all()],
                } for product in products]}, status = 200)
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        
