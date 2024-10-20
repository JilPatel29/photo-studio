# from django.contrib import admin
# from .models import ModelName

# @admin.register(ModelName)
# class ModelNameAdmin(admin.ModelAdmin):
#     list_display = ('field1', 'field2')  # Specify fields to display in the list view
#     search_fields = ('field1',)  # Fields you can search in the admin panel
#     list_filter = ('category',)  # Add filters in the sidebar

# # Register the model along with the custom admin class
# admin.site.register(Service, ServiceAdmin)
from django.contrib import admin
from .models import Service

# Register your model here
admin.site.register(Service)
