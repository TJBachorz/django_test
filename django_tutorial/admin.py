from django.contrib import admin

from .models import Bear, PicnicBasket, Language, Framework

# Register your models here.
admin.site.register(Bear)
admin.site.register(PicnicBasket)
admin.site.register(Language)
admin.site.register(Framework)