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
                    'image_list'    : product.productimage_set.all().first().image_url,#[img.image_url for img in product.productimage_set.all()],
                    'allergy_list'  : [allergies.name for allergies in product.allergy.all()],
                } for product in products]}, status = 200)
            
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)
