"""
URL configuration for playerServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() functions: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from playerWeb import views
from django.views.generic import RedirectView
from django.views.generic import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),             # 主页面，index.html为Vue打包后的入口文件
    path('musicspace/', TemplateView.as_view(template_name='index.html')),  # 用以解决数据更新后的页面刷新报错
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('register/', TemplateView.as_view(template_name='index.html')),
    path('discover/', TemplateView.as_view(template_name='index.html')),    # 用以解决数据更新后的页面刷新报错
    path('api/', include('playerWeb.functions.urls')),                      # 数据交换相关路径，可查看后端数据返回情况
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
