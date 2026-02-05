friend_a = {"python", "cooking", "hiking", "movies"}
friend_b = {"hiking", "gaming", "photography", "python"}
common_interests = friend_a & friend_b
print("common interests:", common_interests)
all_interests = friend_a | friend_b
print("all interests:", all_interests)
a_unique = friend_a - friend_b
print("friend_a unique interests:", a_unique)
