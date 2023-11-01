from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(slider)
admin.site.register(category)
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(product)
class productAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}