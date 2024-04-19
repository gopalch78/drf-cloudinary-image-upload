from django.urls import path
from .views import ImageUploadView
# Register,
urlpatterns = [
    # path("register/", Register.as_view(), name="index"),
    path(
        "image-upload/", ImageUploadView.as_view(), name='image'
    )
]