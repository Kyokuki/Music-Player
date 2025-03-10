from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from playerWeb.models import Music,RelUserMusic,User
from playerWeb.functions.serializer import MusicSerializer,UserSerializer
from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView


class MusicViewSet(viewsets.ModelViewSet):
    """音乐空间 视图"""
    queryset = RelUserMusic.objects.all()
    serializer_class = MusicSerializer

    def list(self, request):
        userid = request.GET.get('userid', None)
        if userid:
            musicid = [item['musicid'] for item in list(self.queryset.filter(userid=userid).values('musicid'))]
        self.queryset = Music.objects.filter(id__in=musicid)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class Discover(viewsets.ModelViewSet):
    """发现音乐 视图"""
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def list(self, request):
        self.queryset = Music.objects.all()
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)


class UserApi(viewsets.ViewSet):
    """用户 视图"""

    # 只有两个参数，默认路由后缀为方法名，可以添加第三个参数url_path='login'指定
    @action(methods=['post'], detail=False)
    def login(self, request):
        """用户登录"""

        # 对象使用.获取，字典使用['key']获取
        user = User.objects.filter(username=request.data['username']).first()
        result = {
            "code": 200,
            "msg": "登录成功",
            "userinfo": "",
        } 
        if user == None:
            result['msg'] = "登陆失败, 用户不存在"
            result['code'] = -1
            return Response(result)
        
        password = user.password

        if password == request.data['password']:
            serializer = UserSerializer(User.objects.filter(username=request.data['username']).first())
            result['userinfo'] = serializer.data
            return Response(result)
        else:
            result['msg'] = "登陆失败，请检查用户名和密码"
            result['code'] = -1
            return Response(result)

    @action(methods=['post'], detail=False)
    def register(self, request):
        """用户注册"""

        username = request.data['username']
        password = request.data['password']
        # 若用户名已注册，报错
        if User.objects.filter(username=request.data['username']).first():
            result = {
                "code": 200,
                "msg": "注册失败, 用户名重复",
                "body": ""
            }
        # 若用户名未注册，注册
        else:
            User.objects.create(username=username,
                                password=password,
                                photo="http://localhost:8000/media/image/default.jpg")
            result = {
                "code": 200,
                "msg": "注册成功",
                "body": ""
            }
        return Response(result)
