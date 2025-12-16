from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Entry
from .forms import EntryForm

def entry_list(request):
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'entries/entry_list.html', {'entries': entries})

def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entries/entry_detail.html', {'entry': entry})

@login_required
def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, "Entrada creada exitosamente.")
            return redirect('entries:entry_detail', pk=entry.pk)
    else:
        form = EntryForm()
    return render(request, 'entries/entry_form.html', {'form': form})

@login_required
def entry_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada actualizada correctamente.")
            return redirect('entries:entry_detail', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entries/entry_form.html', {'form': form})

@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, "Entrada eliminada.")
        return redirect('entries:entry_list')
    return render(request, 'entries/entry_confirm_delete.html', {'entry': entry})
