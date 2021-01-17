from django.contrib import admin
from cms.models import User

#admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'age',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'sex', 'age',)  # 修正リンクでクリックできる項目

admin.site.register(User, UserAdmin)