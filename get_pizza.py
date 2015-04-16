import papajohns
import twitter
def order_pizza(userfile,use_card=False):
    user=papajohns.UserDetail(userfile)
    if user.twitter is not None:
        if twitter.make_tweet(user.twitter) == 1:
            print("Tweeting successful")
        else:
            print("Tweeting returned error")
    else:
        print("No twitter email")
    papajohns.order(user,use_card)
