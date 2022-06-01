from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('pdfmerge/', views.pdf_merge, name='pdfmerge'),
    path('pdfmergedownload/', views.pdf_merge_download, name='pdfmergedownload'),

    path('pdfsplit/', views.pdf_split, name='pdfsplit'),
    path('pdfsplitshow/', views.pdf_split_show, name='pdfsplitshow'),

    path('pdfrotate/', views.pdf_rotate, name='pdfrotate'),
    path('pdfrotateshow/', views.pdf_rotate_show, name='pdfrotateshow'),
    path('pdfrotatedownload/', views.pdf_rotate_download, name='pdfrotatedownload'),

    path('pdfextract/', views.pdf_extract, name='pdfextract'),
    path('pdfextractshow/', views.pdf_extract_show, name='pdfextractshow'),
    path('pdfextractdownload/', views.pdf_extract_download, name='pdfextractdownload'),

    path('pdfwatermark/', views.pdf_watermark, name='pdfwatermark'),
    path('pdfinfo/', views.pdf_info, name='pdfinfo'),
]