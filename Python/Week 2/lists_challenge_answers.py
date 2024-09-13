
# LISTS CHALLENGE
print('*'*3, 'LISTS CHALLENGE', '*'*3)
# 1. Let's practice swapping data in a list.
#    Change the first three items in `nested_list` to new strings: "Yaw", "Akoto", and "Tech".
nested_list = [[1, 16, 86], ["John", "Jane", "Julie"], [True, "England", 10]]

nested_list[0] = "Yaw"
nested_list[1] = "Akoto"
nested_list[2] = "Tech"

#    Print out the new list to see the changes.
print(nested_list)  # This will print ['Yaw', 'Akoto', 'Tech']

# 2. Try adding a new item to the list by accessing an index that doesn't exist yet, e.g., nested_list[3].
#    This will result in an error, as you cannot add an item this way. You can only replace existing items.
#    Adding new items to a list requires special methods, which we will cover later.

nested_list.append('Akoto Tech') # this will work!
print(nested_list)               # ['Yaw', 'Akoto', 'Tech', 'Akoto Tech']

nested_list[3] = 'Akoto Tech' # this will not work
