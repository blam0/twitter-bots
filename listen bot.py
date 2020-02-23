import tweepy
from keys import consumer_token, consumer_secret, Access_token, Access_token_secret

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)
user = api.me()
print(user.name)


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # if status.text.startswith('RT'):
        #     return
        try:
            if status.retweeted_status:
                return
        except AttributeError:
            print('user name-', status.user.name, '|screen name-', status.user.screen_name)
            print(status.created_at)
            print(status.text)
            # print(status)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['keyword'],
                follow=None,
                languages=['en'],
                is_async=False,
                locations=None,
                stall_warnings=False,
                encoding='utf8',
                filter_level=None)
