from django.shortcuts import render


def Recover_Password(request):
    return render(request, 'Diary/access/recover_password.html', locals())