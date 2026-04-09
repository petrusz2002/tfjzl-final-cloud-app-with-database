from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect  # 🔹 kell az átirányításhoz

urlpatterns = [
    # 🔹 Root URL átirányítás az onlinecourse-ra
    path('', lambda request: redirect('onlinecourse:index')),

    # 🔹 Admin
    path('admin/', admin.site.urls),

    # 🔹 OnlineCourse app
    path('onlinecourse/', include('onlinecourse.urls')),
]

# 🔹 Media fájlok (fejlesztéshez)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)