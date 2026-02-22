import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.followMap = {}  # ✅ renamed
        self.post = {}
        self.time = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post:
            self.post[userId] = [(self.time, userId, tweetId)]
        else:
            self.post[userId].append((self.time, userId, tweetId))

        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        ans = []

        followList = self.followMap.get(userId, [])
        followList = set(followList)
        followList.add(userId)

        for uid in followList:
            if uid in self.post:
                idx = len(self.post[uid]) - 1
                (time, userId, tweetId) = self.post[uid][idx]
                heapq.heappush(heap, (time, userId, tweetId, idx))

        while heap and len(ans) < 10:
            (time, userId, tweetId, idx) = heapq.heappop(heap)
            ans.append(tweetId)

            if idx - 1 >= 0:
                (time, userId, tweetId) = self.post[userId][idx - 1]
                heapq.heappush(heap, (time, userId, tweetId, idx - 1))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.followMap:
            self.followMap[followerId] = [followeeId]
        else:
            self.followMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            return

        curr = self.followMap[followerId]
        temp = []
        for i in curr:
            if i != followeeId:
                temp.append(i)

        self.followMap[followerId] = temp


t = Twitter()
t.postTweet(1, 5)
print(t.getNewsFeed(1))
t.follow(1, 2)
t.postTweet(2, 6)
print(t.getNewsFeed(1))
t.unfollow(1, 2)
print(t.getNewsFeed(1))
