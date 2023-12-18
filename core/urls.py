from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lasotuvi/', include('lasotuvi_django.urls'))
]