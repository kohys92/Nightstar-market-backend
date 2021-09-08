import random

from django.views import View
from django.http import JsonResponse

from .models import Product

class ProductViewer(View):  
    def get(self,request):
        try:
            if not Product.objects.all():
                return JsonResponse({'MESSAGE' : 'PRODUCT DOES NOT EXISTS'})
            
            products = Product.objects.all()
            
            return JsonResponse({'products' : [
                {
                    'id'            : product.id,
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
                    'allergy_list'  : [allergies.name for allergies in product.allergy.all()],
                } for product in products]}, status = 200)
            
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

class DetailViewer(View):
    def get(self, request, id):
        try:
            if not Product.objects.filter(id = id).exists():
                return JsonResponse({'MESSAGE' : 'NOT FOUND'}, status = 404)
            
            product = Product.objects.get(id = id)

            main_id          = product.sub_category.main_category_id
            related_products = Product.objects.filter(sub_category__main_category_id = main_id)

            if related_products.count() < 10:
                selected_products = [
                {
                    "image_url" : current_product.productimage_set.first().image_url,
                    "price"     : current_product.price,
                    "name"      : current_product.name
                }
                for current_product in related_products]

            else:
                selected_products = [
                {
                    "image_url" : current_product.productimage_set.first().image_url,
                    "price"     : current_product.price,
                    "name"      : current_product.name
                }
                for current_product in random.sample(list(related_products), 10)]

            return JsonResponse(
                {
                    'id'                : product.id,
                    'name'              : product.name,
                    'price'             : product.price,
                    'discount'          : product.discount,
                    'sales_unit'        : product.sales_unit,
                    'weight'            : product.weight,
                    'shipping_type'     : product.shipping_type,
                    'origin'            : product.origin,
                    'package_type'      : product.package_type,
                    'infomation'        : product.infomation,
                    'created_at'        : product.created_at,
                    'updated_at'        : product.updated_at,
                    'sub_category'      : product.sub_category.name,
                    'main_category'     : product.sub_category.main_category.name,
                    'menu'              : product.sub_category.main_category.menu.name,
                    'image_list'        : [img.image_url for img in product.productimage_set.all()],
                    'allergy_list'      : [allergies.name for allergies in product.allergy.all()],
                    'selected_products' : selected_products,
                }, status = 200
            )

        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)


