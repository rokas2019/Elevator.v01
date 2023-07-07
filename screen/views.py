from django.shortcuts import render
from .models import Screen, Level, CurrentTime, Arrow


def ele_screen(request):
    arrow = Arrow.objects.all()
    current_level = Screen.objects.all()
    current_time = CurrentTime.objects.latest('time')

    context = {
        'arrow': arrow,
        'current_level': current_level,
        'current_time': current_time,

    }

    response = render(request, 'screen/screen.html', context=context)
    return response


def levels_list(request):
    levels = Level.objects.all()
    return render(request, 'level_detail.html', {'levels': levels})


def level_detail(request, pk):
    level = Level.objects.get(pk=pk)
    return render(request, 'level_detail.html', {'level': level})
