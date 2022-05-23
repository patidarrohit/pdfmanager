from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pdfmerge/', views.pdf_merge, name='pdfmerge'),
    path('pdfmergedownload/', views.pdf_merge_download, name='pdfmergedownload'),
    path('pdfsplit/', views.pdf_split, name='pdfsplit'),
    path('pdfrotate/', views.pdf_rotate, name='pdfrotate'),
    path('pdfextract/', views.pdf_extract, name='pdfextract'),
    path('pdfwatermark/', views.pdf_watermark, name='pdfwatermark'),
    path('pdfinfo/', views.pdf_info, name='pdfinfo'),
]