from django.db import models

class Product(models.Model):
    name          = models.CharField(max_length = 45)
    sub_category  = models.ForeignKey('SubCategory', on_delete = models.CASCADE)
    price         = models.FloatField()
    discount      = models.DecimalField(max_digits = 4, decimal_places = 2)
    sales_unit    = models.CharField(max_length = 20)
    weight        = models.CharField(max_length = 10)
    shipping_type = models.CharField(max_length = 20)
    origin        = models.CharField(max_length = 50)
    package_type  = models.CharField(max_length = 20)
    infomation    = models.TextField()
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)
    allergy       = models.ManyToManyField('Allergy')

    class Meta:
        db_table = 'products'

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'allergies'

class ProductImage(models.Model):
    product   = models.ForeignKey('Product', on_delete = models.CASCADE)
    image_url = models.URLField(max_length = 1000)

    class Meta:
        db_table = 'product_images'

class Menu(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'menus'

class MainCategory(models.Model):
    menu = models.ForeignKey('Menu', on_delete = models.CASCADE)
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'main_categories'

class SubCategory(models.Model):
    main_category = models.ForeignKey('MainCategory', on_delete = models.CASCADE)
    name          = models.CharField(max_length = 45)

    class Meta:
        db_table = 'sub_categories'


