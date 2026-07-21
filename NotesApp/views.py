from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import NoteForm
from .models import Note


def home(request):
    return render(request, "NotesApp/home.html")


def note_list(request):
    notes = Note.objects.all()
    return render(request, "NotesApp/note_list.html", {"notes": notes})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, "NotesApp/note_detail.html", {"note": note})


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "NotesApp/note_form.html", {"form": form})


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, "NotesApp/note_form.html", {"form": form})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "NotesApp/note_confirm_delete.html", {"note": note})


def search_notes(request):
    query = request.GET.get("q", "")
    notes = Note.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)) if query else []

    return render(request, "NotesApp/search.html", {"notes": notes})