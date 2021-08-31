from django.db import models

# Create your models here.

class Order(models.Model):
    user         = models.ForeignKey('users.User', on_delete = models.CASCADE)
    order_status = models.CharField(max_length = 45)
    product      = models.ManyToManyField('products.Product', through = 'OrderItem', related_name = 'orders')

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    product  = models.ForeignKey('products.Product', on_delete = models.CASCADE)
    order    = models.ForeignKey('Order', on_delete = models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'order_items'

class OrderStatus(models.Model):
    order_item     = models.ForeignKey('OrderItem', on_delete = models.CASCADE)
    product_status = models.CharField(max_length = 45)

    class Meta:
        db_table = 'order_statuses'
