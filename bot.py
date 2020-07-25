import tweepy
import time

print("Hey! I am a bot!")

#use your own
CONSUMER_KEY = 'enter value'
CONSUMER_SECRET = 'enter value'
ACCESS_KEY = 'enter value'
ACCESS_SECRET = 'enter value'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('Retrieving and replying...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')

    i = 1

    for mention in reversed(mentions):
        last_seen_id = mention.id

        api.update_status('@' + mention.user.screen_name + 
        ' Hello There. I am a bot. This is an automatic reply.', mention.id)
        
        i = i + 1

    store_last_seen_id(last_seen_id, FILE_NAME)
    print('Done Replying')

while(True):
    reply_to_tweets()
    time.sleep(3600)