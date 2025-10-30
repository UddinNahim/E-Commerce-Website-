from django.contrib import admin
from .models import Products,Order

admin.site.site_header ="E-commerce site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

admin.site.register(Products)
admin.site.register(Order)

# Register your models here.
