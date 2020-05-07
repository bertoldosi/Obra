from django.shortcuts import render


def Logout(request):
    return render(request, 'Diary/access/login.html', locals())