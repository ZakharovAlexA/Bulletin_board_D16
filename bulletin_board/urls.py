from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from board.views import ArticleList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete, Responses, \
    ResponseDetail, response_accept, response_reject, ResponseDelete, ResponseCreate, NewsCreate, NewsDetail, NewsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', ArticleList.as_view(), name='articles'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('responses', Responses.as_view(), name='responses'),
    path('response/<int:pk>', ResponseDetail.as_view(), name='response'),
    path('response/<int:pk>/accept', response_accept, name='response_accept'),
    path('response/<int:pk>/reject', response_reject, name='response_reject'),
    path('response/<int:pk>/delete', ResponseDelete.as_view(),  name='response_delete'),
    path('<int:pk>/response_create', ResponseCreate.as_view(), name='response_create'),
    path('news/create', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news'),
    path('news/list', NewsList.as_view(), name='news_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
