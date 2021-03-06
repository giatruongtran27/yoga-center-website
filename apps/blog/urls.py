from django.urls import include, path
from django.conf.urls import url

from apps.blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('<slug>/',
         views.PostDetailView.as_view(), name='detail'),
]
