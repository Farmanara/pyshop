''' import models so you can register and control them in admin panel '''
from django.contrib import admin
from .models import Product,Offer

class OfferAdmin(admin.ModelAdmin):
    ''' display columns in admin panel '''

    list_display=('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    ''' overrides the list display in admin panel,
    the items in the tuple are column titles for the model items in django admin table '''

    list_display=('name','price','stock')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
