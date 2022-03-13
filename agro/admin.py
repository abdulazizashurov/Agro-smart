from django.contrib import admin
from .models import  User as UserModel, Questions, Zonts, Problems, ZontImages
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.register(UserModel)
admin.site.register(Questions)
admin.site.register(Zonts)
admin.site.register(ZontImages)
admin.site.register(Problems)