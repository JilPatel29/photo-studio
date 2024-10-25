from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

    def get_category(self, obj):
        return getattr(obj, 'category', None)
    get_category.short_description = 'Category'

admin.site.register(Service, ServiceAdmin)
