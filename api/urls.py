from django.urls import path
from django.conf.urls.static import static
from .views import ProductoView
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('productos/',ProductoView.as_view(),name='producto_list'),
    path('productos/<int:pk>/', ProductoView.as_view(), name='producto-detail'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
