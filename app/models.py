from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category = models.CharField(max_length=20,unique=True)
    
    def __str__(self):
        return self.category
    
class Product(models.Model):
    title =models.CharField(max_length=20)
    des = models.TextField()
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_img/',null=True,default='product_img/default_img.jpg')
    
    def __str__(self):
        return self.title    