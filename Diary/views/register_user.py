from django.shortcuts import render


def Register_User(request):
    return render(request, 'Diary/user/register_user.html', locals())