class Twitter:
    def __init__(self):
    # Use itertools.count to generate a decreasing sequence of integers for tweets
        self.timer = itertools.count(step=-1)
        # Use defaultdict and deque to store tweets for each user
        self.tweets = collections.defaultdict(deque)
        # Use defaultdict and set to store followees for each user
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet to the left of the deque for the user, along with its timestamp
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        # If the deque for the user has more than 10 tweets, remove the oldest tweet from the right
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        # Merge the tweets of the user's followees (including the user) using heapq.merge
        tweets = list(heapq.merge(
            *(self.tweets[followee] for followee in self.followees[userId] | {userId})))
        # Return the tweet IDs of the 10 most recent tweets
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the set of followees for the follower
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followee from the set of followees for the follower (if the followee exists)
        self.followees[followerId].discard(followeeId)