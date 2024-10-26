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
from .models import Payment
from .models import Blog
from .models import Gallery
from .models import ContactUs
from .models import Package
from .models import Booking
from .models import Testimonial

# Register your model here
admin.site.register(Service)
admin.site.register(Payment)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(ContactUs)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Testimonial)