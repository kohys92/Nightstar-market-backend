import json

from django.http  import JsonResponse
from django.views import View

from products.models import Product, Cart
from orders.models   import Order, OrderItem
from users.models    import User
from user_auth     import authentication

class CartView(View):
    @authentication
    def post(self, request):
        data            = json.loads(request.body)
        current_user_id = request.user

        try:
            user_id           = current_user_id
            product_id        = data['product_id']
            purchase_quantity = data['quantity']

            if not Product.objects.filter(id = product_id).exists():
                return JsonResponse( {'MESSAGE' : 'PRODUCT DOES NOT EXIST'}, status = 400)

            if Cart.objects.filter(user_id = user_id, product_id = product_id).exists():
                current_product                   = Cart.objects.get(product_id = product_id, user_id = user_id)
                current_product_quantity          = current_product.purchase_quantity
                current_product.purchase_quantity = current_product_quantity + int(purchase_quantity)
                current_product.save()

            else:
                Cart.objects.create(
                    user_id           = user_id,
                    product_id        = product_id, 
                    purchase_quantity = purchase_quantity
                    )

            return JsonResponse( {'MESSAGE' : 'CREATED'}, status = 201)

        except KeyError:
            return JsonResponse( {'MESSAGE' : 'KEY ERROR'}, status = 400)

    @authentication
    def get(self, request):
        current_user_id = request.user
        
        carts = Cart.objects.filter(user_id = current_user_id)

        if not carts.exists():
            return JsonResponse( {'MESSAGE' : 'EMPTY CART'}, status = 204)

        res   = []
        for cart in carts:
            product_id = cart.product_id
            
            product = Product.objects.get(id = product_id)

            res.append(
                {
                "product_img"  : product.productimage_set.filter(product_id = product_id).first().image_url,
                "price"        : product.price,
                "name"         : product.name,
                "package_type" : product.package_type[:2],
                "quantity"     : cart.purchase_quantity
                }
            )
        
        return JsonResponse( {'MESSAGE' : res}, status = 201)
