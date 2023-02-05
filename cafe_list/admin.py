from django.contrib import admin
from .models import CafeInfo

class CafeInfoAdmin(admin.ModelAdmin):
    search_fields = ['cafeName']

admin.site.register(CafeInfo, CafeInfoAdmin)