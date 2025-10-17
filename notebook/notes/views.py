from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm


# 🟢 NOT LİSTELEME
class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    ordering = ['-created_at']

    def get_queryset(self):
        """Sadece giriş yapan kullanıcının notlarını getir"""
        return Note.objects.filter(user=self.request.user).order_by('-created_at')


# 🟡 NOT EKLEME
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        """Oluşturulan nota giriş yapan kullanıcıyı bağla"""
        form.instance.user = self.request.user
        messages.success(self.request, "✅ Yeni not başarıyla oluşturuldu.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "⚠️ Not oluşturulamadı, formu kontrol edin.")
        return super().form_invalid(form)


# 🟠 NOT DÜZENLEME
class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

    def test_func(self):
        """Sadece notun sahibi düzenleyebilir"""
        note = self.get_object()
        return note.user == self.request.user

    def form_valid(self, form):
        messages.success(self.request, "✏️ Not başarıyla güncellendi.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "⚠️ Güncelleme başarısız, lütfen formu kontrol edin.")
        return super().form_invalid(form)


# 🔴 NOT SİLME
class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

    def test_func(self):
        """Sadece notun sahibi silebilir"""
        note = self.get_object()
        return note.user == self.request.user

    def delete(self, request, *args, **kwargs):
        """Silme işlemi sonrası bildirim"""
        messages.warning(self.request, "🗑️ Not başarıyla silindi.")
        return super().delete(request, *args, **kwargs)
