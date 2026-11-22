## LESSON 0.1
# List references
a = [1, 2, 3]
b = a
b.append(4)
print(a)
#answer: [1, 2, 3, 4]

# to actaully copy a list
c = [1, 2, 3]
d = c.copy()
d.append(4)
print(c)

#passign a list into function
def modify(lst):
    lst.append(99)

my_list = [1, 2]
modify(my_list)
print(my_list)

# In-Place vs. Returning a new object
arr = [1, 4, 2, 5]
print("after using .sort() we will get",arr.sort())
print("after in-place sorting:",arr)
new_arr = sorted(arr)
print("new sorted list using sorted()",new_arr)


## LESSON 0.2:Strings, Slicing, and the deque (Queue)
#slicing
s = "hello"
print(s[1:3])
print(s[::-1])
print(s[:3])
print(s[3:])

#string manipulation
s1 = ""
for char in ["a", "b", "c"]:   #TC: O(n^2)
    s += char

s2 = "".join(["a","b","c"])    #TC: O(n)

s3 = "hello world , hello python"
print(s3.split())
print(s3.split(","))
print(s3.lower())
print(s3.upper())
print(s3.isalpha())
print(s3.isdigit())

#ASCII value 
print(ord('a'))
print(ord('e')-ord('a'))

#Queues (FIFO) and deque
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.appendleft(0)
q.pop()
q.popleft()


# LESSON 0.3:  Dicts, Sets, and Frequency Counting
#1.set
seen = set()
seen.add(5)        # adds 5
seen.add(5)        # does nothing, 5 is already there

print(seen)

print(5 in seen)   # True (O(1) Lookup)
seen.remove(5)     # removes 5

print(seen)

#2.dict
counts = {}
counts["apple"] = 1
counts["banana"] = 2
print(counts["apple"])  #prints 1

# how to check if a key exists:
if "apple" in counts:
    print("Yes")

# The safe way to get a value (avoids KeyError):
print(counts.get("Orange", 0))   #returns 0 (if "orange is not there, return default 0")

#frequency counting
#manual way
arr = ["a","b","a","c","a"]
counts = {}
for item in arr:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
print(counts)

#short way
from collections import Counter
counts = Counter(["a","b","a","c","a"])