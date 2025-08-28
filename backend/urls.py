from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('otp/', include('otp.urls')),
    path('auth/', include('users.urls')),
    path('notes/', include('notes.urls'))
]
