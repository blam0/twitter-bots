import tweepy
import time

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)
user = api.me()

# Open text file verne.txt (or your chosen file) for reading
my_file = open('verne.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

for line in file_lines: # Add try ... except block to catch and output errors
    try:
        print(line)

        if line != '\n': # Add if statement to ensure that blank lines are skipped
            api.update_status(line)

        else: # Add an else statement with pass to conclude the conditional statement
            pass
    except tweepy.TweepError as e:
        print(e.reason)

time.sleep(5) # Add sleep method to space tweets by n seconds interval