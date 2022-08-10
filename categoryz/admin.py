from django.contrib import admin

from carts.models import cartlist, items
from . models import *
class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
    
admin.site.register(categ,catadmin)
class prodadmin(admin.ModelAdmin):
    
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,prodadmin)
admin.site.register(cartlist)
admin.site.register(items)

# Register your models here.
