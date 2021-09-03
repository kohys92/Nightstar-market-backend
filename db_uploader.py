import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbmarket.settings")
django.setup()

from products.models import *

CSV_PATH_PRODUCTS = 'products/products.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0] != '':
            menu = Menu.objects.create(name = row[0])
        if row[1] != '':
            main_category = MainCategory.objects.create(name = row[1], menu = menu)
        if row[2] != '':
            sub_category = SubCategory.objects.create(name = row[2], main_category = main_category)
        if row[5] == '':
            row[5] = 0.0
            
        product = Product.objects.create(
            name          = row[3], 
            price         = row[4], 
            discount      = row[5], 
            sales_unit    = row[6], 
            weight        = row[7], 
            shipping_type = row[8], 
            origin        = row[9], 
            package_type  = row[10], 
            infomation    = row[11], 
            sub_category  = sub_category)

        ProductImage.objects.create(product = product, image_url = row[12])
        
        allergy_list = row[13].split(',')
        for allergy in allergy_list:
            if not Allergy.objects.filter(name = allergy).exists() and allergy != '':
                Allergy.objects.create(name = allergy)

            


 