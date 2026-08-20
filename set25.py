user1 = {"shewta","minal","shreya","diksha","sayali"}
user2 = {"minal","shreya","dipali","neha"}

print("Mutual friends:", user1 & user2)
print("User 1 only:", user1 - user2)
print("User 2 only:", user2 - user1)
print("Total unique friends:", len(user1 | user2))