from django.shortcuts import render, redirect

from .forms import LevelForm
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


def level_create(request):
    if request.method == 'POST':
        form = LevelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('levels_list')
    else:
        form = LevelForm()
    return render(request, 'level_form.html', {'form': form})


def level_update(request, pk):
    level = Level.objects.get(pk=pk)
    if request.method == 'POST':
        form = LevelForm(request.POST, request.FILES, instance=level)
        if form.is_valid():
            form.save()
            return redirect('levels_list')
    else:
        form = LevelForm(instance=level)
    return render(request, 'level_form.html', {'form': form, 'level': level})


def level_delete(request, pk):
    level = Level.objects.get(pk=pk)
    if request.method == 'POST':
        level.delete()
        return redirect('levels_list')
    return render(request, 'level_confirm_delete.html', {'level': level})