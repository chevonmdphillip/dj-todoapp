from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            show_all_items = List.objects.all()
            messages.success(request, ('Item Created'))
            context = {'all_items': show_all_items}
            return render(request, 'home.html', context)
    else:
        show_all_items = List.objects.all()
        context = {'all_items': show_all_items}
        return render(request, 'home.html', context)


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Deleted'))
    return redirect('home')
