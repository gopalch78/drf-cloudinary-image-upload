from rest_framework import serializers
from .models import Image
# import cloudinary.uploader
# Registration,
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Registration
#         fields = [ 'id', 
#                   'first_name', 'last_name', 'gender',
#                   'date_of_birth', 'country', 'email_address',
#                    'pincode', 'phone_number', 'alternate_phone_number',
#                   'profile_image', 'cloudinary_url', 
#                  ]
       
#         extra_kwargs = {
#     'cloudinary_url': {'read_only': True},
# }

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image','cloudinary_url']
        extra_kwargs = {
    'cloudinary_url': {'read_only': True},
}
      