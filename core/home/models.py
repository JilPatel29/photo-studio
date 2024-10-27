# home/models.py

# from django.db import models

# class ModelName(models.Model):
#     # Define your fields here
#     field1 = models.CharField(max_length=100)
#     field2 = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.field1


from django.db import models

from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name



class Payment(models.Model):
    payment_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50)  # e.g., 'Credit Card', 'PayPal'
    status = models.CharField(max_length=20)  # e.g., 'Pending', 'Completed', 'Failed'

    def __str__(self):
        return f"{self.method} - {self.amount} - {self.status}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title if self.title else "Untitled"
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # Example: '1 hour', '2 hours', 'Full day'
    features = models.TextField()  # List the features of the package

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    package = models.ForeignKey('Package', on_delete=models.CASCADE)  # Link to a package
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date}"
    
class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars rating
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.rating} stars"
    
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'category')
#     search_fields = ('name',)
#     list_filter = ('category',)

#     def get_category(self, obj):
#         return getattr(obj, 'category', None)
#     get_category.short_description = 'Category'

# admin.site.register(Service, ServiceAdmin) 
