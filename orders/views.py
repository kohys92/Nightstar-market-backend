import json

from django.http  import JsonResponse
from django.views import View

from products import Product
from users    import User

class CartView(View):
    data = json.loads(request.body)

    product_id       = data['product_id']
    user_id           = data['user_id']
    purchase_quantity = data['quantity']

    product = Product.objects.get(id = products_id)
    user    = User.objects.get(id = products_id)

    
