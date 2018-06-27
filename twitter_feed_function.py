class User:
    def __init__(self, name, handle):
        self.name = name
        self.handle = handle


class Tweet:
    def __init__(self, user, tweet, handle):
        self.user = user
        self.tweet = tweet
        self.handle = handle


def create_tweet_objects(user):
    with open('tweet.txt', 'r') as tweet_lines:
        lines = tweet_lines.readlines()
        tweets = create_tweets(lines, user)
        return tweets


def create_users(lines):
    users = []
    for line in lines:
        users.append(line.split('follows')[0].strip())
        follows = line.split('follows')[1].strip()
        if not follows == 'Martin, Alan':
            users.append(follows)
    return list(set(users))


def create_tweets(lines, user):
    users = list()
    for line in lines:
        tweet = ''
        custom_handle = '@{0}'.format(line.split('>')[0].strip())
        if user.name == line.split('>')[0].strip():
            tweet = Tweet(
                user,
                line.split('>')[1].strip(),
                handle=user.handle
            )
        if user.name.lower() == 'ward':
            tweet = Tweet(
                user,
                line.split('>')[1].strip(),
                handle=custom_handle.lower()
            )
        users.append(tweet)
    return list(users)


def create_user_objects():
    with open('user.txt', 'r') as user_lines:
        lines = user_lines.readlines()
        users = create_users(lines)
        user_objects = list()
        for user in users:
            handle = '@{0}'.format(user.lower())
            user = User(user, handle)
            user_objects.append(user)
        return user_objects
