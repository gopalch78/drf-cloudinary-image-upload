
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Image

# Registration , 
# ImageSerializer ,
from .serializers import UploadedImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser  
import cloudinary.uploader
# class Register(generics.ListCreateAPIView):
#     parser_classes = (MultiPartParser, FormParser)
#     queryset = Registration.objects.all()
#     serializer_class = ImageSerializer
#     def post(request,serializer):
#         # Get the uploaded file from request data
#         file =request.data.get('image')

#         # Upload image to Cloudinary
#         uploaded_image =cloudinary.uploader.upload(file)

#         # Set the image URL to your model instance
#         serializer.save( cloudinary_url=uploaded_image['url'])
      
     
    #  cloudinary.uploader.upload(request.FILES['file'])
    
    
class ImageUploadView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Image.objects.all()
    serializer_class = UploadedImageSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
    
    # def post(self, request, *args, **kwargs):
    #     serializer =UploadedImageSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # Upload image to Cloudinary
    #         image= request.data['image']
    #         uploaded_image = cloudinary.uploader.upload(image)
            
    #         # Save image details to database
    #         image_instance = Image.objects.create(cloudinary_url=uploaded_image['url'])
    #         serializer =UploadedImageSerializer(image_instance)
            
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            image_cloud = request.data['image']
            uploaded_image = cloudinary.uploader.upload(image_cloud)
          
            image_instance = Image.objects.create(cloudinary_url=uploaded_image['url'],image=image_cloud)
           
            serializer = UploadedImageSerializer(image_instance)
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )