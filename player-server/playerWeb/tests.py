from django.test import TestCase, Client
from rest_framework.test import APIClient
from playerWeb.models import Music, User, RelUserMusic
from playerWeb.functions.serializer import MusicSerializer, UserSerializer
from django.urls import reverse
import json
import os

class MusicViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.music1 = Music.objects.create(name='Music 1')
        self.music2 = Music.objects.create(name='Music 2')
        self.user = User.objects.create(username='testuser', password='testpassword')
        RelUserMusic.objects.create(userid=self.user.id, musicid=self.music1.id)
        RelUserMusic.objects.create(userid=self.user.id, musicid=self.music2.id)

    def test_music_list(self):
        response = self.client.get(f'/api/music/?userid={self.user.id}')
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'Music 1')
        self.assertEqual(data[1]['name'], 'Music 2')

class DiscoverViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.music1 = Music.objects.create(name='Music 1')
        self.music2 = Music.objects.create(name='Music 2')

    def test_discover_list(self):
        response = self.client.get('/api/discover/')
        self.assertEqual(response.status_code, 200)
        data = response.data
        self.assertEqual(len(data), 2)

class UserApiTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_login(self):
        response = self.client.post('/api/user/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['code'], 200)
        self.assertEqual(response.data['msg'], '登录成功')

    def test_register(self):
        response = self.client.post('/api/user/register/', {'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['code'], 200)
        self.assertEqual(response.data['msg'], '注册成功')


class FileUploadTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.music_upload_url = reverse('upload_music')  # 假设你的视图名为 'upload_music'
        self.image_upload_url = reverse('upload_image')  # 假设你的视图名为 'upload_image'
        # 创建测试用户
        self.test_user = User.objects.create(username='testuser')

class MusicUploadTestCase(FileUploadTestCase):
    def test_upload_music(self):
        with open('playerWeb/testfiles/testMusic.mp3', 'rb') as test_file:
            response = self.client.post(self.music_upload_url, {
                'file': test_file,
                'userid': self.test_user.id
            })
        self.assertEqual(response.status_code, 200)  # 检查是否返回了正确的状态码
        # 检查音乐文件是否被正确上传
        self.assertTrue(os.path.exists('playerWeb/media/audio/testMusic.mp3'))
        # 检查数据库中的音乐记录
        music = Music.objects.last()
        self.assertEqual(music.url, "http://localhost:8000/media/audio/testMusic.mp3")
        # 检查用户与音乐的关联
        rel_user_music = RelUserMusic.objects.last()
        self.assertEqual(rel_user_music.userid, self.test_user.id)
        self.assertEqual(rel_user_music.musicid, music.id)

class ImageUploadTestCase(FileUploadTestCase):
    def test_upload_image(self):
        with open('playerWeb/testfiles/testImage.jpg', 'rb') as test_file:
            response = self.client.post(self.image_upload_url, {
                'file': test_file,
                'userid': self.test_user.id
            })
        self.assertEqual(response.status_code, 200)  # 检查是否返回了正确的状态码
        # 检查图片文件是否被正确上传
        self.assertTrue(os.path.exists('playerWeb/media/image/testImage.jpg'))
        # 检查用户头像是否更新
        self.test_user.refresh_from_db()
        self.assertEqual(self.test_user.photo, "http://localhost:8000/media/image/testImage.jpg")

class DeleteMusicTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.delete_music_url = reverse('delete_music')  # 假设你的视图名为 'delete_music'
        # 创建测试用户和音乐
        self.test_user = User.objects.create(username='testuser')
        self.test_music = Music.objects.create(
            artist='Test Artist',
            name='Test Music',
            url="http://localhost:8000/media/audio/testMusic.mp3"
        )
        RelUserMusic.objects.create(userid=self.test_user.id, musicid=self.test_music.id)

    def test_delete_music(self):
        # 发送POST请求来删除音乐
        response = self.client.post(self.delete_music_url, json.dumps({'userid': self.test_user.id, 'musicid': self.test_music.id}), content_type='application/json')
        self.assertEqual(response.status_code, 200)  # 检查是否返回了正确的状态码
        # 检查音乐和关联记录是否被删除
        self.assertFalse(Music.objects.filter(id=self.test_music.id).exists())
        self.assertFalse(RelUserMusic.objects.filter(userid=self.test_user.id, musicid=self.test_music.id).exists())
        # 检查文件是否被删除
        self.assertFalse(os.path.exists('playerWeb/media/audio/testMusic.mp3'))
