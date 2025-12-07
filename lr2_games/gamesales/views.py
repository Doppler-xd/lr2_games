from django.shortcuts import render
from .forms import GameAdForm 
from .models import GameAd, Genre
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
class GameAdCreateView(LoginRequiredMixin, CreateView):
    model = GameAd
    form_class = GameAdForm
    template_name = 'gamesales/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class GameAdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GameAd
    form_class = GameAdForm
    template_name = 'gamesales/edit.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class GameAdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GameAd
    template_name = 'gamesales/delete_confirm.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class GameAdListView(ListView):
    model = GameAd
    template_name = 'gamesales/index.html'
    context_object_name = 'ads'
    paginate_by = 10  # пагинация
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_genre'] = Genre.objects.get(pk=self.kwargs['genre_id'])
        context['platforms'] = GameAd.PLATFORM_CHOICES
        context['all_genres'] = Genre.objects.all()
        return context
class GameAdByGenreView(ListView):
    template_name = 'gamesales/index.html'
    context_object_name = 'ads'
    paginate_by = 10

    def get_queryset(self):
        genre_id = self.kwargs['genre_id']
        return GameAd.objects.filter(genre_id=genre_id).order_by('-published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_genre'] = Genre.objects.get(pk=self.kwargs['genre_id'])
        context['platforms'] = GameAd.PLATFORM_CHOICES
        context['all_genres'] = Genre.objects.all()
        return context
class GameAdCreateView(CreateView):
    model = GameAd
    form_class = GameAdForm
    template_name = 'gamesales/create.html'
    success_url = reverse_lazy('index')
    def get_queryset(self):
        queryset = GameAd.objects.all()
        query = self.request.GET.get('q')
        platform_list = self.request.GET.getlist('platforms')  # ← получаем список платформ

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        if platform_list:
            queryset = queryset.filter(platform__in=platform_list)

        return queryset.order_by('-published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['platforms'] = GameAd.PLATFORM_CHOICES
        context['query'] = self.request.GET.get('q', '')
        context['selected_platforms'] = self.request.GET.getlist('platforms')  # ← передаём в шаблон
        context['all_genres'] = Genre.objects.all()
        return context
def index(request):
    ads = GameAd.objects.all()
    return render(request, 'gamesales/index.html', {'ads': ads})
# Create your views here.
