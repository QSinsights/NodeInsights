from django.shortcuts import render, redirect
from .models import VS1H1
from .forms import VS2H1
from django.contrib import messages

def V2H1(request):

    if request.method == 'POST':
        form = VS2H1(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = VS1H1.objects.all()
            messages.success(request, ('New item added..'))
            return render(request, 'V2H1.html', {'all_items':all_items})

    else:
        all_items = VS1H1.objects.all()
        return render(request, 'V2H1.html', {'all_items':all_items})

def delete(request, list_id):

    item = VS1H1.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted..'))
    return redirect('V2H1')

def home (request):
    return render(request, 'index.html')
