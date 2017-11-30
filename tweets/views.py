from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from .twitter_api import search_twitter

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# from .models import Tweet
# from .serializers import TweetSerializer


# Create your views here.
# class TweetList(APIView):
#
#     def get(self, request):
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass

def index(request):
    return render(request, 'tweets/index.html', context={})

def search(request):
    tweets = search_twitter(request)
    return render(request, 'tweets/index.html', context={'tweets':tweets})
