from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Words
from .forms import BookWordMultiForm

# def IndexView(request):
#     return render(request, 'wisesaying/index.html',{})
class IndexView(ListView):
    model = Words
    template_name = 'wisesaying/index.html'
    queryset = Words.objects.order_by('-created_at')
    paginate_by = 4

class detailView(DetailView):
    model = Words

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'wisesaying/signup.html', {'form': form})

class postSearch(ListView):
    template_name = 'wisesaying/search.html'
    context_object_name = 'search_text'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(postSearch, self).get_context_data(**kwargs)
        context['q'] = self.request.GET['q']
        return context

    def get_queryset(self):
        q = self.request.GET['q']
        return Words.objects.filter(word__icontains=q)

# def addWord(request):
#     form = BookWordMultiForm()
#     return render(request, 'wisesaying/post.html', {'form':form})
class AddWord(CreateView):
    form_class = BookWordMultiForm
    success_url = reverse_lazy('wisesaying:index')
    template_name = 'wisesaying/post.html'

    def form_valid(self, form):
        book = form['book'].save()
        word = form['word'].save(commit=False)
        word.book = book
        word.save()
        return redirect(self.success_url)