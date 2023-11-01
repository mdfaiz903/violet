from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(slider)
admin.site.register(Category)
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(Product)
class productAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}