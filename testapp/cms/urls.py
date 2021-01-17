from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # User
    path('user/', views.user_list, name='user_list'),   # 一覧
    path('user/add/', views.user_edit, name='user_add'),  # 登録
    path('user/mod/<int:user_id>/', views.user_edit, name='user_mod'),  # 修正
    path('user/del/<int:user_id>/', views.user_del, name='user_del'),   # 削除
]