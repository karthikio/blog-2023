from django.urls import path
from .views import postListView, postsDetailView, postCreateView, postDeleteView, postEditView, postSearchView, feedbackPage


urlpatterns = [
  path('', postListView, name='post_list_page'),
  path('post/search/', postSearchView, name='post_search_page'),
  path('post/create/', postCreateView, name='post_create_page'),
  path('post/<slug:slug>/', postsDetailView, name='post_detail_page'),
  path('post/edit/<slug:slug>/', postEditView, name='post_edit_page'),
  path('post/delete/<slug:slug>/', postDeleteView, name='post_delete_page'),
  path('posts/feedback/', feedbackPage, name='feedback_page')
]