from django.shortcuts import render


def Login(request):
    return render(request, 'Diary/access/login.html', locals())