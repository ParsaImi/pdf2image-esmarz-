from django.urls import path

from . import views

urlpatterns = [
    path("", views.convert_pdf_to_images, name="convert_pdf_to_images"),
]