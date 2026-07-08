print("--- Dictionary Methods ---")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"Original dictionary: {my_dict}")

# 1. get()
print(f"Value for key 'b' using get(): {my_dict.get('b')}")

# 2. keys()
print(f"Keys: {my_dict.keys()}")

# 3. values()
print(f"Values: {my_dict.values()}")

# 4. items()
print(f"Items: {my_dict.items()}")

# 5. update()
my_dict.update({'d': 4})
print(f"After update: {my_dict}")


print("\n--- List Methods ---")
my_list = [10, 20, 30, 20, 40]
print(f"Original list: {my_list}")

# 1. append()
my_list.append(50)
print(f"After append(50): {my_list}")

# 2. insert()
my_list.insert(1, 15)
print(f"After insert(1, 15): {my_list}")

# 3. remove()
my_list.remove(20) # Removes first occurrence
print(f"After remove(20): {my_list}")

# 4. pop()
popped_item = my_list.pop()
print(f"After pop() (removed {popped_item}): {my_list}")

# 5. count()
print(f"Count of 20: {my_list.count(20)}")


print("\n--- Tuple Methods/Operations ---")
my_tuple = (1, 2, 3, 2, 4, 5)
print(f"Original tuple: {my_tuple}")

# 1. count()
print(f"Count of 2: {my_tuple.count(2)}")

# 2. index()
print(f"Index of 4: {my_tuple.index(4)}")

# 3. Slicing (common operation)
print(f"Sliced tuple (1:4): {my_tuple[1:4]}")

# 4. Concatenation (common operation)
new_tuple = my_tuple + (6, 7)
print(f"Concatenated tuple: {new_tuple}")

# 5. Unpacking (common operation)
a, b, *rest = my_tuple
print(f"Unpacked (a, b, rest): {a}, {b}, {rest}")


print("\n--- Set Methods ---")
my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7}
print(f"Original set: {my_set}")
print(f"Other set: {other_set}")

# 1. add()
my_set.add(6)
print(f"After add(6): {my_set}")

# 2. remove()
my_set.remove(1)
print(f"After remove(1): {my_set}")

# 3. union()
print(f"Union with other_set: {my_set.union(other_set)}")

# 4. intersection()
print(f"Intersection with other_set: {my_set.intersection(other_set)}")

# 5. difference()
print(f"Difference with other_set: {my_set.difference(other_set)}")










print("--- Dictionary Methods ---")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"Original dictionary: {my_dict}")

# 1. get()
print(f"Value for key 'b' using get(): {my_dict.get('b')}")

# 2. keys()
print(f"Keys: {my_dict.keys()}")

# 3. values()
print(f"Values: {my_dict.values()}")

# 4. items()
print(f"Items: {my_dict.items()}")

# 5. update()
my_dict.update({'d': 4})
print(f"After update: {my_dict}")


print("\n--- List Methods ---")
my_list = [10, 20, 30, 20, 40]
print(f"Original list: {my_list}")

# 1. append()
my_list.append(50)
print(f"After append(50): {my_list}")

# 2. insert()
my_list.insert(1, 15)
print(f"After insert(1, 15): {my_list}")

# 3. remove()
my_list.remove(20) # Removes first occurrence
print(f"After remove(20): {my_list}")

# 4. pop()
popped_item = my_list.pop()
print(f"After pop() (removed {popped_item}): {my_list}")

# 5. count()
print(f"Count of 20: {my_list.count(20)}")


print("\n--- Tuple Methods/Operations ---")
my_tuple = (1, 2, 3, 2, 4, 5)
print(f"Original tuple: {my_tuple}")

# 1. count()
print(f"Count of 2: {my_tuple.count(2)}")

# 2. index()
print(f"Index of 4: {my_tuple.index(4)}")

# 3. Slicing (common operation)
print(f"Sliced tuple (1:4): {my_tuple[1:4]}")

# 4. Concatenation (common operation)
new_tuple = my_tuple + (6, 7)
print(f"Concatenated tuple: {new_tuple}")

# 5. Unpacking (common operation)
a, b, *rest = my_tuple
print(f"Unpacked (a, b, rest): {a}, {b}, {rest}")


print("\n--- Set Methods ---")
my_set = {1, 2, 3, 4, 5}
other_set = {4, 5, 6, 7}
print(f"Original set: {my_set}")
print(f"Other set: {other_set}")

# 1. add()
my_set.add(6)
print(f"After add(6): {my_set}")

# 2. remove()
my_set.remove(1)
print(f"After remove(1): {my_set}")

# 3. union()
print(f"Union with other_set: {my_set.union(other_set)}")

# 4. intersection()
print(f"Intersection with other_set: {my_set.intersection(other_set)}")

# 5. difference()
print(f"Difference with other_set: {my_set.difference(other_set)}")







# Example of 'break'
for i in range(1, 10):
    if i == 5:
        print(f"Breaking loop at i = {i}")
        break # Exit the loop when i is 5
    print(f"Current value: {i}")
print("Loop finished.")




# Example of 'continue'
for i in range(1, 10):
    if i % 2 == 0: # Skip even numbers
        print(f"Continuing (skipping even number): {i}")
        continue # Skip the rest of the code in this iteration for even numbers
    print(f"Current odd value: {i}")
print("Loop finished.")


# Example of 'pass'
# You might use pass when defining a function but haven't implemented it yet
def coming_soon_function():
    pass # This function does nothing for now

print("Calling coming_soon_function():")
coming_soon_function()
print("Function called, nothing happened.")

# Or in a loop where you want to do nothing for certain conditions
for i in range(1, 5):
    if i == 3:
        print(f"Encountered 3, doing nothing with pass.")
        pass # Do nothing when i is 3
    else:
        print(f"Processing value: {i}")







# Example of 'pass'
# You might use pass when defining a function but haven't implemented it yet
def coming_soon_function():
    pass # This function does nothing for now

print("Calling coming_soon_function():")
coming_soon_function()
print("Function called, nothing happened.")

# Or in a loop where you want to do nothing for certain conditions
for i in range(1, 5):
    if i == 3:
        print(f"Encountered 3, doing nothing with pass.")
        pass # Do nothing when i is 3
    else:
        print(f"Processing value: {i}")



# --- range() function ---
print("\n--- range() Function ---")
# Generates a sequence of numbers, often used for looping a specific number of times.
print("Numbers from 0 to 4 using range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")

print("Numbers from 2 to 7 with step 2 using range(2, 8, 2):")
for i in range(2, 8, 2):
    print(i, end=" ")
print("\n")

# --- len() function ---
print("\n--- len() Function ---")
# Returns the number of items in an object (length).
my_string = "Hello Python"
my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3)

print(f"Length of string '{my_string}': {len(my_string)}")
print(f"Length of list {my_list}: {len(my_list)}")
print(f"Length of tuple {my_tuple}: {len(my_tuple)}")

# --- type() function ---
print("\n--- type() Function ---")
# Returns the type of an object.
var_int = 10
var_float = 3.14
var_str = "Python"
var_list = [1, 2, 3]
var_bool = True

print(f"Type of {var_int}: {type(var_int)}")
print(f"Type of {var_float}: {type(var_float)}")
print(f"Type of '{var_str}': {type(var_str)}")
print(f"Type of {var_list}: {type(var_list)}")
print(f"Type of {var_bool}: {type(var_bool)}")





# --- 'for' loop example ---
print("\n--- 'for' Loop ---")
# Iterating over a list of items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterating a specific number of times using range()
print("Counting from 0 to 4:")
for i in range(5):
    print(i)

# --- 'while' loop example ---
print("\n--- 'while' Loop ---")
# Repeating a block of code as long as a condition is true
count = 0
while count < 3:
    print(f"The count is: {count}")
    count += 1 # Increment count to eventually stop the loop
print("While loop finished.")

