import unittest

from twitter_feed_function import (
    User, Tweet
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


        # def test_isupper(self):
        #     self.assertTrue('FOO'.isupper())
        #     self.assertFalse('Foo'.isupper())
        #
        # def test_split(self):
        #     s = 'hello world'
        #     self.assertEqual(s.split(), ['hello', 'world'])
        #     # check that s.split fails when the separator is not a string
        #     with self.assertRaises(TypeError):
        #         s.split(2)


if __name__ == '__main__':
    unittest.main()
