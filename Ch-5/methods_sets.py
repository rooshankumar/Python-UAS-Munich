# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set1:", set1)
print("Set2:", set2)

# add() → Add an element
set1.add(10)
print("After adding 10 to set1:", set1)

# remove() → Remove an element (raises error if not found)
set1.remove(2)
print("After removing 2 from set1:", set1)

# discard() → Remove an element safely
set1.discard(100)  # Does nothing as 100 is not in the set
print("After discarding 100 from set1:", set1)

# pop() → Remove and return an arbitrary element
removed_element = set1.pop()
print("Popped element:", removed_element)
print("Set1 after popping:", set1)

# clear() → Clear all elements
set_copy = set1.copy()  # Copying before clearing
set1.clear()
print("Set1 after clearing:", set1)
print("Copy of set1:", set_copy)

# union() → Combine sets
combined = set_copy.union(set2)
print("Union of set_copy and set2:", combined)

# intersection() → Common elements
common = set_copy.intersection(set2)
print("Intersection of set_copy and set2:", common)

# difference() → Elements in set_copy but not in set2
diff = set_copy.difference(set2)
print("Difference of set_copy from set2:", diff)

# issubset() → Check if one set is a subset of another
print("Is common a subset of set2?", common.issubset(set2))

# issuperset() → Check if one set is a superset of another
print("Is set2 a superset of common?", set2.issuperset(common))
