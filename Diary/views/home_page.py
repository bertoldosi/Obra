from django.shortcuts import render


def Index(request):
    return render(request, 'Diary/index.html', locals())