from twitter_feed_function import (
    create_tweet_objects,
    sorted_users
)


def main_function():
    sort_users = sorted_users()

    for user in sort_users:
        print(user.name)
        tweets = create_tweet_objects(user)
        for tweet in tweets:
            if tweet != '':
                print('{0}: {1}'.format(tweet.handle, tweet.tweet))


if __name__ == '__main__':
    main_function()
