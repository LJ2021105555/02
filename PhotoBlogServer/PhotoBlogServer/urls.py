"""
URL configuration for PhotoBlogServer project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views as blog_views
from rest_framework.authtoken import views as drf_views
from django.conf import settings
from django.conf.urls.static import static

# 设置默认路由
router = DefaultRouter()
router.register(r'posts', blog_views.DetectionViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", drf_views.obtain_auth_token, name="api_token_auth"),
    path("api_root/", include(router.urls)),  # 添加 api_root 端点
    path("", blog_views.detection_list, name='detection_list'),  # 首页展示检测结果
]

# 添加媒体文件的 URL 支持
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
