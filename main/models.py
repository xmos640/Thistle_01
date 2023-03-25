from django.db import models

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
    comment = models. TextField(max_length=5000)
    rate = models. IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return str(self.product_name+" "+str(self.rate)+" stars") 

# class likes(models.Model):
#     pro
    