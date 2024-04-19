from django.db import models



# class Registration(models.Model):
    
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]
#     profile_image = models.ImageField(upload_to='images/',blank=True)
#     cloudinary_url = models.URLField(blank=True) 
#     first_name = models.CharField(max_length=100,default=True)
#     last_name = models.CharField(max_length=100,default=True) 
#     gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
#     date_of_birth = models.DateField(blank=True, null=True)
#     country = models.CharField(max_length=100,default=True)
#     email_address = models.EmailField(max_length=100,default=True)
#     pincode = models.CharField(max_length=20,default=True)
#     phone_number = models.CharField(max_length=20,default=True)
#     alternate_phone_number = models.CharField(max_length=20, blank=True, null=True)
   
    
    
#     def __str__(self):
#         return self.username  
    
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/') 
    cloudinary_url = models.URLField(blank=True)  