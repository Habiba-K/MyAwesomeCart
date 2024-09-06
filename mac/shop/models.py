from django.db import models

# Create your models here.
class Product(models.Model):
    Mobile_id = models.AutoField
    Mobile_name = models.CharField(max_length=50)
    Memory = models.CharField(max_length=50, default="")
    Processor = models.CharField(max_length=50, default="")
    Camera = models.CharField(max_length=100, default="")
    Messaging = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=300)
    Other_features = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.Mobile_name

# Create your Contact models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
   

    def __str__(self):
        return self.name

 # Create your Orders models here.     
class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add = True)

    def _str_(self):
        return self.update_desc[0:7] + "..."