from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ArticleForm, ResponseForm, NewsForm
from .models import Article, UserResponse, News


class ArticleList(ListView):
    model = Article
    ordering = '-dateCreation'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_resp = UserResponse.objects.filter(article__id=self.request.resolver_match.kwargs['pk'])
        context['article_resp'] = article_resp
        return context


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_article',)
    form_class = ArticleForm
    model = Article
    template_name = 'article_create.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        return super().form_valid(form)


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_article',)
    form_class = ArticleForm
    model = Article
    template_name = 'article_update.html'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_article',)
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles')


class Responses(LoginRequiredMixin, ListView):
    raise_exception = True
    model = UserResponse
    ordering = '-dateCreation'
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myresp = UserResponse.objects.filter(article__author=self.request.user)
        context['myresp'] = myresp
        return context


class ResponseDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = UserResponse
    template_name = 'response.html'
    context_object_name = 'response'


@login_required
@csrf_protect
def response_accept(request, pk):
    resp = UserResponse.objects.get(id=pk)
    resp.status = True
    resp.save()
    return render(request, 'response_accept.html')


@login_required
@csrf_protect
def response_reject(request, pk):
    resp = UserResponse.objects.get(id=pk)
    resp.status = False
    resp.save()
    return render(request, 'response_reject.html')


class ResponseDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = UserResponse
    template_name = 'response_delete.html'
    success_url = reverse_lazy('responses')


class ResponseCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ResponseForm
    model = UserResponse
    template_name = 'response_create.html'
    success_url = reverse_lazy('responses')

    def form_valid(self, form):
        response = form.save(commit=False)
        response.article = Article.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        response.responseAuthor = self.request.user
        return super().form_valid(form)


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('board.add_news',)
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.author = self.request.user
        return super().form_valid(form)


class NewsDetail(DetailView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'


class NewsList(ListView):
    model = News
    ordering = '-dateCreation'
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10
