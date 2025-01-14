from django.contrib import admin
from .models import Item
from .models import SiteSetting

admin.site.register(Item)
admin.site.register(SiteSetting)
