import base64
import requests
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Query

"""
Performs a query or looks through returned results.
"""
def search_twitter(request):

    tweets_json = None
    tweets = []

    # Perform query if POST
    if request.method == 'POST':
        tweets_json = get_twitter_json(request)

        for t in tweets_json['statuses']:
            tweet_data = {
                'profile_pic': t['user']['profile_image_url'],
                'name': t['user']['name'],
                'handle': t['user']['screen_name'],
                'text': t['text'],
                'favorites': t['user']['favourites_count'],
                'retweets': t['retweet_count'],
                'date': t['user']['created_at'],
            }
            tweets.append(tweet_data)

        tweets = sorted(tweets, key = lambda t: t['favorites'] + t['retweets'], reverse=True)

        import os
        from innerspace.settings import BASE_DIR
        os.chdir(os.path.join(BASE_DIR,'tweets'))

        f = open('tweets100.json', 'w+')
        tweets_json_pretty = json.dumps(tweets, indent=2, separators=(',',':'))
        f.write(tweets_json_pretty)
        f.close()

    elif request.method == 'GET':
        f = open('tweets100.json', 'r')
        tweets = json.load(f)


    # Display up to 20 pages of tweets


    page = request.GET.get('page', 1)
    paginator = Paginator(tweets, 10)

    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)

    return tweets


"""
Perform a Twitter API query.
"""
def get_twitter_json(request):
    # Key setup
    client_key = '1PGki11r3iVCbV4T9Pie1RWjP'
    client_secret = 'g2mGl0cd4cJfh1gXmRIJfaQO4Q2YIiBxKDUCm0ohycSV8DNCys'

    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret).decode('ascii')
    base_url = 'https://api.twitter.com/'


    # Authentication setup
    auth_url = '{}oauth2/token'.format(base_url)

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }


    # Get bearer access token
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    assert auth_resp.status_code == 200

    token_type = auth_resp.json()['token_type']
    token_itself = auth_resp.json()['access_token']


    # Perform query
    search_headers = {
        'Authorization': 'Bearer {}'.format(token_itself)
    }

    query = request.POST['usr_query']

    search_params = {
        'q': query,
        'result_type': 'recent',
        'count': 100
    }

    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    assert search_resp.status_code == 200


    # Extract tweets from json
    tweet_json = search_resp.json()
    tweet_json_pretty = json.dumps(tweet_json, indent=2, separators=(',',':'))

    return tweet_json
