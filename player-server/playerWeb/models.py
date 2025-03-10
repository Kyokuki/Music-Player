from django.db import models


class Music(models.Model):
    """歌曲列表"""
    id = models.AutoField(primary_key=True)     # 歌曲ID
    artist = models.CharField(max_length=255)   # 歌手
    name = models.CharField(max_length=255)     # 歌曲名
    url = models.URLField(max_length=256)       # 文件路径


class RelUserMusic(models.Model):
    """用户-歌曲关系列表"""
    userid = models.IntegerField()      # 用户ID
    musicid = models.IntegerField()     # 歌曲ID


class User(models.Model):
    """用户列表"""
    id = models.AutoField(primary_key=True)                         # 用户ID
    username = models.CharField(max_length=10,default="test")       # 用户名
    password = models.CharField(max_length=10,default="password")   # 用户密码
    photo = models.URLField(max_length=256, blank=True)             # 用户头像
