import tweepy
import random
auth = tweepy.OAuthHandler("aYFy76da9sIiKE1fvPHDk0g04", "WEJRcjRSXXYBLjPv8Yd1Jl52ad2LAcORHew9sEI8DpRUJ9QiN1")
auth.set_access_token("3173400849-YzK5LEyUafJCbekegCSPANyoBqfdgOVvRUTTQQI", "kwHh7w2Q35dOdbsJKqYBOOyyWjmhdImXuRSVTHBxmYfab")
api = tweepy.API(auth)
api.home_timeline()
def make_tweet(twitter_id,account=api,full_name=None,msg="{0} just ordered a delicious, hot steamy pizza with Pizza Button"):
    try:
        account.update_status(status=msg.format('@'+twitter_id)+"("+str(random.randint(0,1000))+")")
        return 1
    except tweepy.TweepError as e:
        print(e.args)
        return -1

