from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views as blog_views  # 导入现有的 views 文件中的内容

# 创建默认的 API 路由器并注册视图集
router = DefaultRouter()
router.register(r'detections', blog_views.DetectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # 注册 API 端点
    path('admin/', admin.site.urls),  # 管理页面
    path('', blog_views.detection_list, name='detection_list'),  # 网页渲染视图
]



