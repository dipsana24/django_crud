from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

# READ: list all notes
def note_list(request):
    """View to list all notes, ordered by newest first."""
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

# READ: single note detail
def note_detail(request, pk):
    """View to show details of a single note."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

# CREATE
def note_create(request):
    """View to create a new note."""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')  # name from urls
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'type': 'Create'})

# UPDATE
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'type': 'Update'})

# DELETE
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})