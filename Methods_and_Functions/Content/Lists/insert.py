"""
list.insert(i, x)

Description: Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
"""

my_list = ["one", "three", 4.0, 6]
my_list.insert(0, 0)  # Inserting 0 in the position 0
print(my_list)  # [0, "one", "three", 4.0, 6]
my_list.insert(2, "two")  # Inserting "two" in the position 2
print(my_list)  # [0, "one", "two", "three", 4.0, 6]
my_list.insert(5, "5")  # Inserting "5" in the position 5
print(my_list)  # [0, "one", "two", "three", 4.0, "5", 6]
my_list.insert(len(my_list)+1, "seven")  # Inserting "seven" in the last position.
print(my_list)  # [0, "one", "two", "three", 4.0, "5", 6, "seven"]

#If you need to insert an element to the very end of the list is better to use .append(x) function.
