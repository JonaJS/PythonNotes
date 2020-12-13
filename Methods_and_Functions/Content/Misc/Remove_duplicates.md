# Removing duplicates from a list with set and dict.fromkeys(lst).

## set(lst)
A duplicate is an element that appears more than once in a list. For example, **2** is a duplicate in **[1, 2, 2]**.

Call **set(a_list)** with a list as **a_list** to create a set containing the unique elements of the list. Use **list(a_set)** with the new set as a_set to convert back to a list.
``` Python
a_list = [1, 2, 2]
a_set = set(a_list) #Get unique elements
no_duplicates = list(a_set) #Convert set to list
print(no_duplicates)
```
_**OUTPUT**_
``` Python
[1, 2]
```

## dict.fromkeys(lst)

**_If maintaining the order of the elements is necessary_**, call **dict.fromkeys(iterable)** _with a **list** as **iterable**_ to create a dictionary containing the unique elements of the list as keys. Use **list(a_dict)** to _with the new dictionary as **a_dict**_ to convert back to a list containing only the keys.
``` Python
a_list = [1, 2, 2]
a_dictionary = dict.fromkeys(a_list) #Create dictionary
no_duplicates = list(a_dictionary) #Convert dictionary to list
print(no_duplicates)
```
_OUTPUT_
``` Python
[1, 2]
```
