from django.db import models
from django.contrib.auth.models import AbstractUser

class user_type(models.Model):
    user_ty = models.CharField(max_length=200)

class User(AbstractUser):
    user_t = models.ForeignKey(user_type,on_delete=models.SET_NULL,blank=True,null=True)
    user_image = models.ImageField(upload_to='user_pic/',blank=True,null=True)

class category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_img = models.ImageField(upload_to='category/',blank=True,null=True,)

class product(models.Model):
    product_name = models.CharField(max_length=200)
    product_old_price = models.FloatField()
    product_new_price = models.FloatField()
    product_description = models.TextField()
    cat = models.ForeignKey(category,on_delete=models.SET_NULL,blank=True,null=20, related_name='category')

class product_image(models.Model):
    product_image = models.ImageField(upload_to='product_image/',blank=True,null=True)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE,related_name='prod')


class customer(models.Model):
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    mobile = models.CharField(max_length=15)
    password= models.CharField(max_length=200)

    @staticmethod
    def customer_check(user_name):
        try:
            return customer.objects.get(username = user_name)
        except:
            return False

