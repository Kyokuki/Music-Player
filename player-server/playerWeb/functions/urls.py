from django.urls import path, include
from rest_framework.routers import DefaultRouter
from playerWeb import views
from playerWeb.functions import upload, delete

"""路由"""
router = DefaultRouter()
router.register('music', views.MusicViewSet)                            # 音乐空间视图的数据传递
router.register('user', views.UserApi, basename='userapi')              # 用户相关视图的数据传递
router.register('discover', views.Discover, basename='discoverapi')     # 发现音乐视图的数据传递

urlpatterns = [
    path('', include(router.urls)),
    path('uploadmusic/', upload.upload_music, name='upload_music'),     # 上传歌曲的数据传递
    path('uploadimage/', upload.upload_image, name='upload_image'),     # 上传头像的数据传递
    path('deletemusic/', delete.delete_music, name='delete_music'),     # 删除歌曲的数据传递
]
