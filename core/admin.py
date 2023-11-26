from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, Updates

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_user', 'custom_method')
    list_filter = ('location',)

    def custom_method(self, obj):
        return obj.bio

    custom_method.short_description = 'Custom Bio'

admin.site.register(Profile, ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at', 'no_of_likes')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    search_fields = ('user', 'caption')

admin.site.register(Post, PostAdmin)

class LikePostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'username')

admin.site.register(LikePost, LikePostAdmin)

class FollowersCountAdmin(admin.ModelAdmin):
    list_display = ('follower', 'user')

admin.site.register(FollowersCount, FollowersCountAdmin)

class UpdatesAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    readonly_fields = ('date',)

admin.site.register(Updates, UpdatesAdmin)
