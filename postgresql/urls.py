
from django.contrib import admin
from django.urls import path
from sql.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    
]
