# This class demonstrates the members and features of a dictionary data structure in Python.
# There are 11 methods are available in dictionary data structure.
# 1.get() 2.items() 3.keys() 4.values() 5.pop() 6.popitem() 7.clear() 8.update(dictionary)
# 9.copy() 10.fromkeys(iterable,value) 11.setdefault(dictionary)

# Empty dictionary
d1 = {}
print(d1)
print(type(d1))

# Dictionary keys must be immutable type such as string, number, tuple, frozenset etc.
d1_String = {"key1": "value1", "key2": "value2"}
print(d1_String)

d1_Integer = {1: "value1", 2: "value2"}
print(d1_Integer)

d1_Tuple = {(1, 2): "value1", (3, 4): "value2"}
print(d1_Tuple)

d1_Frozenset = {frozenset([1, 2]): "value1", frozenset([3, 4]): "value2"}
print(d1_Frozenset)

# 1.get() method returns the value of the specified key.
print("String Dictionary is:",d1_String)
print('d1_String.get("key1")',d1_String.get("key1"))

# 2.items() method returns a list containing a tuple for each key value pair.
print("String Dictionary items are:",d1_String.items())

# 3.keys() method returns a list containing the dictionary's keys.
print("String Dictionary keys are:",d1_String.keys())

# 4.values() method returns a list of all the values in the dictionary.
print("String Dictionary values are:",d1_String.values())

# 5.pop(key) method removes the element with the specified key.
print("String Dictionary before pop(key1) is:",d1_String)
d1_String.pop("key1")
print("String Dictionary after pop(key1) is:",d1_String)

# 6.popitem() method removes the last inserted key-value pair.
print("String Dictionary before popitem:",d1_String)
d1_String.popitem()
print("String Dictionary after popitem:",d1_String)

# 7.clear() method removes all the elements from the dictionary.
print("String Dictionary before clear:",d1_String)
d1_String.clear()
print("String Dictionary after clear:",d1_String)

# 8.update(dictionary) method updates the dictionary with the specified key-value pairs.
print("String Dictionary before update:",d1_String)
d1_String.update({"key3": "value3", "key4": "value4"})
print("String Dictionary after update:",d1_String)

# 9.copy() method returns a copy of the dictionary.
print("String Dictionary before copy:",d1_String)
d1_String_copy = d1_String.copy()
print("String Dictionary after copy:",d1_String_copy)

# 10.fromkeys() method returns a dictionary with the specified keys and values.
print("String Dictionary before fromkeys:",d1_String)
d1_String_fromkeys = dict.fromkeys(["key5", "key6"], "value")
print("String Dictionary after fromkeys:",d1_String_fromkeys)

# 11.setdefault(key,value) method returns the value of the specified key. If the key does not exist, insert the key, with the specified value.
print("String Dictionary before setdefault:",d1_String)
d1_String.setdefault("key7", "value7")
print("String Dictionary after setdefault:",d1_String)