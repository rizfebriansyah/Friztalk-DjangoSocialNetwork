from django.urls import path
from .views import post_remark_create_and_list_view, love_dislike_post, UserPostDeleteView, UserPostUpdateView

app_name = 'postings'

urlpatterns = [
    path('', post_remark_create_and_list_view, name='main-post-view'),
    path('loved/', love_dislike_post, name='love-post-view'),
    path('<pk>/delete/', UserPostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update/', UserPostUpdateView.as_view(), name='post-update'),
]