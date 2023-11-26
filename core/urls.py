from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ProfileApi, PostApi

router = routers.DefaultRouter()
router.register(r'profile', ProfileApi)
router.register(r'post', PostApi)

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('api/', include(router.urls))
]