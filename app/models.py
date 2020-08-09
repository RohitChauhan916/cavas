from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    template_name = models.CharField(max_length=200)

    def __str__(self):
        return self.template_name

class Canvas(models.Model):
    canvas_id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=100)
    design_image = models.ImageField(upload_to='canvas', null=True, blank=True)

    def __str__(self):
        return str(self.canvas_id)