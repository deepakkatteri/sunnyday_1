from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User,Permission


# Create your models here.
class Product_Category(models.Model):
    Product_Gen_Name=models.TextField(max_length=20)
    Product_Disp_Image=models.ImageField(default='')
    def __str__(self):
        return self.Product_Gen_Name

class Product(models.Model):
    Product_Category=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    Product_Name=models.TextField(max_length=20)
    Product_Model=models.TextField(max_length=20)
    Product_Image=models.ImageField()
    Product_Description_Para1=models.TextField(max_length=500)
    Product_Description_Para2=models.TextField(max_length=500)
    def __str__(self):
        return self.Product_Name


class Blog(models.Model):
    Date=models.DateField(default=datetime.now(),blank=True)
    Topic=models.TextField(max_length=200)
    Blog_Image=models.ImageField()
    Content_para_1=models.TextField(max_length=700)
    Content_para_2=models.TextField(max_length=700)
    Content_para_3=models.TextField(max_length=700)
    Content_para_4=models.TextField(max_length=700)
    Content_para_5=models.TextField(max_length=700)
    def __str__(self):
        return self.Topic

class Research(models.Model):
	Research_Topic=models.TextField(max_length=200)
	Research_Description=models.TextField(max_length=300)
	def __str__(self):
            return self.Research_Topic
class Research_TimeLine(models.Model):
	Research=models.ForeignKey(Research,on_delete=models.CASCADE)
	Date=models.DateField(default=datetime.now(),blank=True)
	Activity=models.TextField(default=datetime.now(),blank=True)
	def __str__(self):
            return self.Research

class News(models.Model):
	Date=models.DateField(default=datetime.now(),blank=True)
	News_Topic=models.TextField(max_length=200)
	News_Content=models.TextField(max_length=500)
	def __str__(self):
            return self.News_Topic

class Order(models.Model):
    Name=models.TextField(max_length=15)
    PhoneNo=models.TextField(max_length=10)
    Emailid=models.TextField(max_length=50)
    def __str__(self):
            return self.PhoneNo

class Category(models.Model):
    class Meta:
        permissions=(
        ("sales_staff","sales staff"),
        ("sales_man","sales manager"),
        ("admin","administrator"),
        ("design","desin_staff"),
        ("tech","tech_manager"),
        ("accountman","accounts_manager"),
        ("accounts","accounts_staff"),
        ("purchase","purchase_staff"),
        ("purchaseman","purchase_manager"),
        )

class Pds(models.Model):
    CustomerName=models.TextField(max_length=15)
    DateofEnquiry=models.DateField(auto_now=True)
    Address=models.TextField(max_length=50)
    Phone=models.TextField(max_length=10)
    Email=models.TextField(max_lenth=50)
    EnquirySource=models.TextField(max_length=20)
    DealerName=models.TextField(max_length=15,blank=True)
    ReferencePerson=models.Text(max_length=10,blank=True)
    Section=models.TextField(max_length=15,blank=True)
    Choices={
    (OFF-GRID,'OFF_GRID'),
    (GRID-TIED,'GRID-TIED'),
    (GRID-TIED_WITH_BACKUP,'GRID-TIED-WITH-BACKUP'),
    (STREETLIGHT,'STREETLIGHT')
    }





# class User(mod.User):
#     Name=mod.User.username
#     Password=mod.User.password
