
# from termios import CINTR
from pyexpat import model
from django.db import models
import datetime

# Create your models here.

# Shop Login
class Shop_login(models.Model):
    Email  = models.EmailField(max_length=25)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'shop_login'

del_choices=(
    ('y','yes'),
    ('n','no'),
)

# date = datetime.datetime.now()
# current_date = date
# Shop Profile or Full Details
class Shop_profile(models.Model):
    #foreign Key
    Shop_login = models.ForeignKey(Shop_login, on_delete=models.CASCADE)
    
    # id = models.AutoField(primary_key=True)

    # Shop Basic Details
    ShopImage = models.FileField(upload_to="images/shops", default="images/shop.png")
    owner_name = models.CharField(max_length=25, default="")
    ShopName = models.CharField(max_length=25, default="")
    Delivery = models.CharField(max_length=10,choices=del_choices)
    Contact = models.CharField(max_length=12, default="")
    Shop_type = models.CharField(max_length=25, default="")
    DOJ = models.DateField(auto_now=True)

    #Shop Address
    Shop_no = models.CharField(max_length=25, default="")
    Shop_complex = models.CharField(max_length=25, default="")
    City = models.CharField(max_length=25, default="")
    State = models.CharField(max_length=25, default="")
    Pincode = models.CharField(max_length=25, default="")
    Address = models.TextField(max_length=250, default="")
    

    class Meta:
        db_table = 'shop_profile'

#Customer Login
class Master(models.Model):
    Email = models.CharField(max_length=25)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'

gender_choices = (
    ('m','male'),
    ('f','female'),
)

#Customer Profile or Full Details
class Profile(models.Model):
    # profileimage = models.FileField(upload_to="images/shops", default="images/shop.png")
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to="images/users", default="images/user.png")
    FullName = models.CharField(max_length=25, default="")
    DOB = models.DateField(auto_created=True, default="2022-01-01")
    Gender = models.CharField(max_length=10,choices=gender_choices)
    Contact = models.CharField(max_length=12, default="")
    
    #Address
    House_no = models.CharField(max_length=25, default="")
    Complex_name = models.CharField(max_length=25, default="")
    City = models.CharField(max_length=25, default="")
    State = models.CharField(max_length=25, default="")
    Pincode = models.CharField(max_length=25, default="")
    Address = models.TextField(max_length=250, default="")
    
    class Meta:
        db_table = 'profile'

# Shop Types
class Shop_type(models.Model):
    Shop_type = models.CharField(max_length=25, default="")
    class Meta:
        db_table = 'Shop_type'

# Product Types
class Product_type(models.Model):
    Product_type = models.CharField(max_length=25, default="")
    class Meta:
        db_table = 'Product_type'



availability =(
    ('y','yes'),
    ('n','no'),
)
# Shop Products
class Product(models.Model):
    Product_Image = models.FileField(upload_to="images/users", default="images/product.png")
    # Shop_profile = models.ForeignKey(Shop_profile, on_delete=models.CASCADE)
    Profile_id = models.ForeignKey(Shop_profile, on_delete=models.CASCADE)
    Prod_name = models.CharField(max_length=25, default="")
    Prod_type = models.CharField(max_length=25, default="")
    Prod_price = models.FloatField(max_length=25, default="")
    Prod_des = models.TextField(max_length=255, default="")
    Availability = models.CharField(max_length=10,choices=availability)
    class Meta:
        db_table = 'Product'

# State
class State(models.Model):
    State = models.CharField(max_length=25, default="")
    class Meta:
        db_table = 'state'

# City
class City(models.Model):
    State = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=25, default="")
    class Meta:
        db_table = 'city'

