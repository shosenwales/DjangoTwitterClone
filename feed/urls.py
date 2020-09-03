from django.urls import path
from . import views
from .views import TweetListView,TweetCreateView,TweetDeleteView

urlpatterns = [
   path('', TweetListView.as_view(), name='index'),
   path('create/',TweetCreateView.as_view(), name='tweetcreate'),
   path('tweet/<int:pk>/delete',TweetDeleteView.as_view(), name='tweetdelete'),
]
