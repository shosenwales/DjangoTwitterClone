from django.shortcuts import render
from .models import tweet
from django.contrib.auth.decorators import login_required

tweets = tweet.objects.all
# Create your views here.
@login_required
def index(request):
    context = {
        'tweets': tweets
    }
    return render(request, 'feed/index.html', context)