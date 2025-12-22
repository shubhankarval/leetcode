"""
Problem: Design Twitter
Difficulty: Medium
URL: https://leetcode.com/problems/design-twitter/

Time Complexity: O(F) for getNewsFeed(), O(1) for postTweet(), follow(), unfollow()
where F is the number of followees of the user

Space Complexity: O(N²) where N is the number of users
"""

from collections import defaultdict, deque
import heapq


class Twitter:

    def __init__(self):
        self.time = 0  # time of tweet being posted
        self.following = defaultdict(set)  # user -> set of who user is following
        self.feed = defaultdict(deque)  # user -> queue of tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].appendleft([self.time, tweetId])
        if len(self.feed[userId]) > 10:
            self.feed[userId].pop()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)

        heap = []
        for user in self.following[userId]:
            for time, tweetId in self.feed[user]:
                if len(heap) < 10 or time > heap[0][0]:
                    heapq.heappush(heap, [time, tweetId])
                    if len(heap) > 10:
                        heapq.heappop(heap)

        res = deque([])
        while len(heap):
            res.appendleft(heapq.heappop(heap)[1])
        return list(res)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
