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
        tweets = create_tweets_list(lines, user)
        return tweets


def create_users(lines):
    users = []
    for line in lines:
        users.append(line.split('follows')[0].strip())
        follows = line.split('follows')[1].strip()
        if not follows == 'Martin, Alan':
            users.append(follows)
    return list(set(users))


def create_tweets_list(lines, user):
    users = list()
    for line in lines:
        tweet = ''
        custom_handle = '@{0}'.format(line.split('>')[0].strip())
        if user.name == line.split('>')[0].strip():
            tweet = Tweet(
                user,
                tweet=trim_tweet_greater_140(line),
                handle=user.handle
            )
        if user.name.lower() == 'ward':
            tweet = Tweet(
                user,
                tweet=trim_tweet_greater_140(line),
                handle=custom_handle.lower()
            )
        users.append(tweet)
    return list(users)


def trim_tweet_greater_140(line):
    _tweet = line.split('>')[1].strip()
    if len(_tweet) > 141:
        _tweet = _tweet[:140]
    return _tweet


def create_users_list():
    with open('user.txt', 'r') as user_lines:
        lines = user_lines.readlines()
        users = create_users(lines)
        user_objects = list()
        for user in users:
            handle = '@{0}'.format(user.lower())
            user = User(user, handle)
            user_objects.append(user)
        return user_objects


def sorted_users():
    users = create_users_list()
    users.sort(key=lambda x: x.name, reverse=False)
    return users
