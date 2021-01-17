from django.contrib import admin
from django.urls import path, include #URL追加の時に書く

urlpatterns = [
    path('cms/', include('cms.urls')),   # ←ここを追加
    path('admin/', admin.site.urls),
]
