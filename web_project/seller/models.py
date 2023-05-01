from django.db import models

# Create your models here.
class Seller(models.Model):
    full_name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length = 15)
    address = models.TextField(max_length =255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    pic = models.FileField(upload_to = 'profile_pics', default ='sad.jpg')

    def __str__(self):
        return self.email
    
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    des = models.TextField(max_length=255)
    price = models.FloatField(default=10.0)
    product_stock = models.IntegerField(default=0)
    pic = models.FileField(default='sad.jpg', upload_to='product_pics')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name