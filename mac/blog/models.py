from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name=models.CharField(max_length = 255)
    email=models.CharField(max_length = 100)
    phone = models.CharField(max_length = 13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add = True,blank=True)

    def __str__(self):
        return 'Message from ' + self.name

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
    image = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return self.Mobile_name       