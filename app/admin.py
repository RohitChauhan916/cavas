from django.contrib import admin
from .models import Canvas, Category
from .models import User
# Register your models here.

admin.site.register(Category)
admin.site.register(Canvas)