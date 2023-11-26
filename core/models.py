from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField("ID пользователя")
    bio = models.TextField("Био", blank=True)
    profileimg = models.ImageField("Фото профиля",upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField("Локация",max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField("Имя",max_length=100)
    image = models.ImageField("Фото",upload_to='post_images')
    caption = models.TextField("Текст поста")
    created_at = models.DateTimeField("Время добавления",default=datetime.now)
    no_of_likes = models.IntegerField("Кол-во лайков",default=0)
    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField("ID поста", max_length=500)
    username = models.CharField("Имя пользователя",max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField("Подписчик", max_length=100)
    user = models.CharField("Пользователь",max_length=100)

    def __str__(self):
        return self.user
    

class Updates(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now); 
    def __str__(self):
        return self.text