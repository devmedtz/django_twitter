import tweepy
from django.shortcuts import render
from django.conf import settings


consumer_key= settings.CONSUMER_KEY
consumer_secret= settings.CONSUMER_SECRET
access_token= settings.ACCESS_TOKEN
access_token_secret= settings.ACCESS_TOKEN_SECRET


def is_valid_queryparam(param):
    return param != '' and param is not None

def twitter_home(request):

    if request.method == 'GET':
        search_qry = request.GET.get('hashtag')
        search_qrys = str(search_qry)

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        if is_valid_queryparam(search_qrys):
            popular_tweets = tweepy.Cursor(api.search, q=search_qrys, lang="en", result_type="popular").items(50)

    context = {
        'popular_tweets':popular_tweets,
    }

    return render(request, 'index.html', context)
