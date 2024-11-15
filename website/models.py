from django.db import models
from adminpanel.models import product, customer

class add_to_cart(models.Model):
    product_id = models.ForeignKey(product,on_delete=models.SET_NULL,blank=True,null=True, related_name='products')
    customer_id = models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    cart_date = models.DateField(auto_now=True)
    cart_status = models.BooleanField(default=True)


class checkout(models.Model):
    customer_info = models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    checkout_date = models.DateTimeField(auto_now=True)
    cart_item = models.ManyToManyField(add_to_cart, related_name='cart_list')


