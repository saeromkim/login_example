from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('check_id/', views.check_id),
    path('a/', views.index2),
    path('register_member_db/', views.register_member_db),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
