from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

admin.site.register(Service, ServiceAdmin)
