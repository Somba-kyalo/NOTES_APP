from django.shortcuts import get_object_or_404, render
from NotesApp.models import Note
from .services import generate_summary


def summarize_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    summary = generate_summary(note.content)

    return render(request, "NotesApp/ai_summary.html", {"note": note, "summary": summary})