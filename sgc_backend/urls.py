# sgc_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('frontend.urls')),  # 모든 뷰는 frontend.urls에서 관리
]
