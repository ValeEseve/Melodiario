from django.shortcuts import render

# Create your views here.
def entry_list(request):
    return render(request, 'entries/entry_list.html')

def entry_detail(request, pk):
    return render(request, 'entries/entry_detail.html', {'pk': pk})

def entry_create(request):
    return render(request, 'entries/entry_form.html')

def entry_update(request, pk):
    return render(request, 'entries/entry_form.html', {'pk': pk})

def entry_delete(request, pk):
    return render(request, 'entries/entry_confirm_delete.html', {'pk': pk})

