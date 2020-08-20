from django.shortcuts import render
from .models import tweet

tweets = tweet.objects.all
# Create your views here.
def index(request):
    context = {
        'tweets': tweets
    }
    return render(request, 'feed/index.html', context)