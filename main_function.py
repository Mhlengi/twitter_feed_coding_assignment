from twitter_feed_function import (
    create_tweet_objects,
    create_user_objects
)


def main_function():
    users = create_user_objects()
    users.sort(key=lambda x: x.name, reverse=False)
    for user in users:
        print(user.name)
        tweets = create_tweet_objects(user)
        for t in tweets:
            if t != '':
                print('{0}: {1}'.format(t.handle, t.tweet))


if __name__ == '__main__':
    main_function()
