from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from cms.models import User
from cms.forms import UserForm


def user_list(request):
    """UserList"""
#return HttpResponse('Userの一覧')
    users = User.objects.all().order_by('id')
    return render(request,
                  'cms/user_list.html',     # 使用するテンプレート
                  {'users': users})         # テンプレートに渡すデータ


def user_edit(request, user_id=None):
    """Userの編集"""
    #return HttpResponse('Userの編集')
    if user_id:   # user_id が指定されている (修正時)
        user = get_object_or_404(User, pk=user_id)
    else:         # user_id が指定されていない (追加時)
        user = User()

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            user = form.save(commit=False)
            user.save()
            return redirect('cms:user_list')
    else:    # GET の時
        form = UserForm(instance=user)  # user インスタンスからフォームを作成

    return render(request, 'cms/user_edit.html', dict(form=form, user_id=user_id))


def user_del(request, user_id):
    """Userの削除"""
    #return HttpResponse('Userの削除')
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('cms:user_list')
