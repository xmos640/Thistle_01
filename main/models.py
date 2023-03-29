from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50,default="")
    size = models.CharField(max_length=200,default="")
    mrp = models.IntegerField( default=0)
    sale_price = models.IntegerField(default ="")
    desc = models.CharField(max_length=5000,default="")
    desc2 = models.CharField(max_length=5000,default='')
    pub_date = models.DateField()
    image = models.FileField(upload_to="images/",default="")
    availabilty = models.IntegerField(default=1)
    directions = models.CharField(max_length=4000,default="")
    # likes = 
     
    # sale_name = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.product_name
    
class prod_images(models.Model):
    prod = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

class sales(models.Model):
    discount= models.IntegerField()
    # category = 
    # bxgx = 

class Review(models.Model):
    # user = models. ForeignKey (User, models.CASCADE)
    product =  models.CharField(max_length=100,default="")
    email = models.CharField(max_length=250,default="")
    user_review = models.CharField(max_length=3000,primary_key=True) 
    name = models.CharField(max_length=250,default="")
    product_name=models.CharField(max_length=100,default="")
    comment = models.TextField(max_length=5000)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return str(self.product_name+" "+str(self.rate)+" stars") 
    


class CouponCode(models.Model):
    coupon = models.CharField(max_length=100,default="")
    used_by = models.ManyToManyField(User,default="")
    discount= models.IntegerField(default=0)
    validity = models.DateTimeField(default=now)
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=2000, default="")
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100 , default="")
    email = models.CharField(max_length=300, default="")
    Address = models.CharField(max_length=1000, default="")
    postal_code = models.CharField(max_length=20, default="")
    phone_number = models.CharField(max_length=20,default="")
    coupon_used = models.CharField(max_length=50,default="")
    instructions = models.CharField(max_length=2000,default="")
    city = models.CharField(max_length=200,default="")
    payment_ref =models.CharField(max_length=25,default='')
    delivered = models.IntegerField(default=0)
    dispatched = models.IntegerField(default=0)
    payment_conf = models.IntegerField(default=0)
    timestamp= models.DateField(auto_now_add= True)
    link = models.CharField(max_length=5000,default='nil')
    declined = models.IntegerField(default=0)
    delivery_date = models.DateField(default=now)
    def __str__(self): 
        return str(self.name + str(self.amount))
    
