from rest_framework import viewsets
from .models import Detection
from .serializers import DetectionSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser

# 用于 REST API 的视图集
class DetectionViewSet(viewsets.ModelViewSet):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer
    authentication_classes = [TokenAuthentication]  # Token 认证
    permission_classes = [IsAuthenticated]  # 只允许已认证的用户访问
    parser_classes = (MultiPartParser, FormParser)  # 支持多部分文件上传

# 用于网页渲染的列表视图
def detection_list(request):
    detections = Detection.objects.all()
    return render(request, 'blog/detection_list.html', {'detections': detections})

