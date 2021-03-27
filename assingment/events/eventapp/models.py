from django.db import models

# Create your models here.
class event_template(models.Model):
     pid = models.AutoField(primary_key=True)
     day = models.CharField(default="",max_length=6)
     month = models.CharField(default="",max_length=16)
     start_time = models.CharField(default="",max_length=16)
     end_time = models.CharField(default="",max_length=16)
     location = models.CharField(default="",max_length=26)
     name = models.CharField(default="",max_length=100)
     image1 = models.ImageField(upload_to="images/",default="")
     def __int__(self):
        return self.pid

class like_template(models.Model):
     pid = models.AutoField(primary_key=True)
     ids = models.CharField(default="",max_length=6)
     day = models.CharField(default="",max_length=6)
     month = models.CharField(default="",max_length=16)
     start_time = models.CharField(default="",max_length=16)
     end_time = models.CharField(default="",max_length=16)
     location = models.CharField(default="",max_length=26)
     name = models.CharField(default="",max_length=100)
     image1 = models.ImageField(upload_to="images/",default="")
     def __int__(self):
        return self.pid