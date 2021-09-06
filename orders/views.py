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
        data        = json.loads(request.body)
        cur_user_id = request.user

        try:
            user_id           = cur_user_id
            product_id        = data['product_id']
            purchase_quantity = data['quantity']
            if not Product.objects.filter(id = product_id).exists():
                return JsonResponse( {'MESSAGE' : 'DOES NOT EXIST'}, status = 400)

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
        cur_user_id = request.user
        
        carts = Cart.objects.filter(user_id = cur_user_id)
        res   = []
        for cart in carts:
            product_id = cart.product_id
            if not Product.objects.filter(id = product_id).exists():
                return JsonResponse({'MESSAGE' : 'NO ITEM'}, status = 400)
            
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

class OrderView(View):
    @authentication
    def post(self, request):
        data = json.loads(request.body)
        
        cur_user_id = request.user

        try:
            products = data['products']
            
            order = Order.objects.create(
                    user_id      = cur_user_id,
                    order_status = '주문 완료',
            )

            for product in products:
                product_id = product['product_id']
                quantity   = product['quantity']

                OrderItem.objects.create(
                    product_id           = product_id,
                    order_id             = order.id,
                    quantity             = quantity,
                    order_item_status_id = "1"
                )

            return JsonResponse( {'MESSAGE' : 'CREATED'}, status = 201)

        except KeyError:
            return JsonResponse( {'MESSAGE' : 'KEY ERROR'}, status = 400)
