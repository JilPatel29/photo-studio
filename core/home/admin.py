from django.contrib import admin
from .models import ModelName

@admin.register(ModelName)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Specify fields to display in the list view
    search_fields = ('field1',)  # Fields you can search in the admin panel
