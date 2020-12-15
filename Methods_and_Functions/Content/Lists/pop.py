"""
list.pop([i])

Description: Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
"""


my_list = [0, "one", "two", "three", 4.0, "5", 6, "seven"]
item_popped = my_list.pop()  # .pop() returns the value of the item popped and we can assign it into a variable
print(item_popped)  # "seven"
print(my_list)  # [0, "one", "two", "three", 4.0, "5", 6]
item_popped_2 = my_list.pop(0)  # here we're popping the item in the index 0
print(item_popped)  # 0
print(my_list)  # ["one", "two", "three", 4.0, "5", 6]
item_popped_3 = my_list.pop(2)
print(item_popped_3)  # "three"
print(my_list)  # ["one", "two", 4.0, "5", 6]
