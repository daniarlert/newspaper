from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    SearchResultsListView,
)

urlpatterns = [
    path("<uuid:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<uuid:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<uuid:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("", ArticleListView.as_view(), name="article_list"),
]
