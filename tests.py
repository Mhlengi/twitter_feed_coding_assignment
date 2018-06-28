import unittest

from twitter_feed_function import (
    create_tweet_objects,
    create_tweets_list,
    create_users,
    create_users_list,
    trim_tweet_greater_140,
    sorted_users,
    User,
    Tweet
)


class TestObjectClass(unittest.TestCase):
    def test_user_creation(self):
        user_alan = User(
            name='Alan',
            handle='@alan'
        )

        self.assertEqual(user_alan.name, 'Alan')
        self.assertEqual(user_alan.handle, '@alan')

    def test_tweet_creation(self):
        user_alan = User(
            name='Alan',
            handle='@alan'
        )
        alan_tweet = Tweet(
            user=user_alan,
            handle='@alan',
            tweet='tweet message'
        )

        self.assertEqual(alan_tweet.user.name, 'Alan')
        self.assertEqual(alan_tweet.handle, '@alan')
        self.assertEqual(alan_tweet.tweet, 'tweet message')


class TestCustomFunction(unittest.TestCase):
    def test_trim_tweet_greater_140(self):
        line = 'Ward> There are only two hard things in ' \
               'Computer Science: cache invalidation, ' \
               'naming things and off-by-1 errors.'
        trim_tweet = trim_tweet_greater_140(line)
        expected_trim_tweet = 'There are only two hard things in ' \
                              'Computer Science: cache invalidation, ' \
                              'naming things and off-by-1 errors.'

        self.assertEqual(trim_tweet, expected_trim_tweet)

    def test_create_users(self):
        lines = ['Ward follows Alan']
        users = create_users(lines)
        expected_users = ['Alan', 'Ward']

        self.assertEqual(sorted(users), expected_users)

    def test_create_tweet_objects(self):
        user = User(
            name='Alan',
            handle='@alan'
        )

        self.assertEqual(create_tweet_objects(user)[0].user.name, user.name)

    def test_create_tweets_list(self):
        user = User(
            name='Alan',
            handle='@alan'
        )
        lines = []
        create_tweets_list(lines, user=user)

        self.assertEqual(create_tweets_list(lines, user=user), [])

    def test_create_users_list(self):
        create_users_list()

        self.assertTrue(create_users_list())

    def test_sorted_users(self):
        User(
            name='Alan',
            handle='@alan'
        )

        self.assertTrue(sorted_users())


if __name__ == '__main__':
    unittest.main()
