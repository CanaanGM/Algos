"""
    The Datastructure one:
Design a simplified version of Twitter where 
1. users can post tweets,
2. follow/unfollow another user 
3. is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
1. Twitter) Initializes your twitter object.
METHODS:

1. void postTweet (int userId, Int tweetId) 
     Composes a new tweet with ID tweetId by the user userld.
     Each call to this function will be made with a unique tweetId.

2. List <Integer> getNewsFeed (int userId)
     Retrieves the 10 most recent tweet IDs in the user's news feed. 
     Each item in the news feed must be posted by users who the user followed or by the user themself. 
     Tweets must be ordered from most recent to least recent

3. void follow(int followerId, int followeeId)
     The user with ID followerId started following the user with ID followeeId.

4. void unfollow(int followerld, int followeeId) 
     The user with ID followerld started unfollowing the user with followeeId.
ID

"""


from collections import deque

from Oldimpls.doubly_linked_list import DoublyLinkedList


class Twitter():
    def __init__(self) -> None:
        self.users = {
            # Canaan : []
            # Ali : []
            # . . . .
        }
        self.tweets = {
            # Canaan : [ tweet A, tweet B]
        }

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        """
        Creates a new tweet objects with the unique id: twitter id
        """
        if user_id not in self.tweets.keys():
            self.tweets[user_id] = []

        self.tweets[user_id] = tweet_id
        

    def get_news_feed(self, user_id: int) -> list:
        """
            need to check the graph for folowed users
            if there's a relation get me their tweets
            otherwise fill my feed with stuff i made (myId == tweet.user_id)
        """    
        user_graph = self.users.get(user_id)

        news_feed = []

        for followed_user in user_graph:
            news_feed.append(self.tweets[followed_user])
        print(news_feed)
        

        

    def follow(self, user_id, follwee_id):
        """
            creates the relation in our graph
            directional graph
        """
        if user_id in self.users.keys() \
            and follwee_id in self.users.keys():
            
            self.users[user_id].append(follwee_id)
            self.users[follwee_id].append(user_id)
            return True
        return False



    def un_follow(self, user_id, folowee_id):
        """
        removes the relation from the graph
        """
        if user_id in self.users.keys() \
        and folowee_id in self.users.keys():
            if folowee_id in self.users[user_id]:
                self.users[user_id].remove(folowee_id)
            if user_id in self.users[folowee_id]:
                self.users[folowee_id].remove(user_id)
            return True
        return False
    

    def signup(self, user_id):
        """creates the user """
        if user_id not in self.users.keys():
            self.users[user_id] = []
            return True
        return False
    
    def print_graph(self):
        for v in self.users:
            print(f"{v} : {self.users[v]}")
            


t = Twitter()
t.signup("Canaan")
t.signup("Ali")
t.signup("Dante")
t.signup("Vergil")

t.follow("Canaan", "Ali")
t.follow("Canaan", "Dante")
t.follow("Ali", "Dante")
t.follow("Ali", "Vergil")
# t.print_graph()

# t.un_follow("Canaan", "Ali")
# t.print_graph()


t.post_tweet("Canaan", "1")
t.post_tweet("Canaan", "2")
t.post_tweet("Vergil", "why aren't u motivated ? ")
t.post_tweet("Dante", "where pizza ")
t.post_tweet("Ali", "i helped u solve it")
print(t.tweets)

# feed = []

# for tweet in t.tweets:
#     # if ALI in vergil : [Ali]
#     # print ALi's Tweet
#     # print(tweet)
#     # print(tweet["user_id"] , t.users[tweet["user_id"]] )
#     if "Canaan" in t.users[tweet["user_id"]]:
#         # print(tweet["user_id"])
#         feed.append(t.tweets.pop())
#         print(tweet)


t.get_news_feed("Canaan")

things = [1,2,3,4,56,7,8,1,2,3,4,56,7,8]

# print(things[-10::])




users = {
    "Canaan": {  "dante": "???" , "Ali": "???"  }و
    "ِAli": {  "dante": "???" , "Ali": "???"  }و
    "Ahamad": {  "dante": "???" , "Ali": "???"  }و
}