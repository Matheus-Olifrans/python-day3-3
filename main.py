nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
user_friends.add(input('tell me your friends'))
# Add the name to the empty set
print(user_friends.intersection(nearby_people))