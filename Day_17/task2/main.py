# syntax to create class -  class NameOfClass:
class User:     #class created
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # print("new user being created...")

    def follow(self, user):
        user.follower += 1
        user.following +=1


user_1 = User("001", "angela")
user_2 = User("002", "Jack")
print(user_1.id)


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# user_1 = User()  # object created
# user_1.id = "001" #add attribute to object
# user_1.username = "angela"
#
# print(user_1.username)
#
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jack"