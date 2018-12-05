from django.contrib import admin
from .models import Form, Category, Skills

admin.site.register(Category)
admin.site.register(Skills)
admin.site.register(Form)