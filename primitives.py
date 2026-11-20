#variable, types, printing
x = 5
y = 3.14
s = "hello"
b = True
print(x, s)

#Lists (arrays)
a = [1, 2, 3]
a[0]
a[-1]
len(a)
a.append(4)
a.pop()
a[1] = 99

#loops
for x in [10, 20, 30]:
    print(x)

for i in range(3):
    print(i)

while x > 0:
    x -= 1

#if/else
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")

#functions
def add(a, b):
    return a+b

print(add(3, 4))

#dict and set
d = {"a": 1, "b": 2}
d["a"]
d["c"] = 3
print("a" in d)

s = {1, 2, 3}
print(2 in s)

#example
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

print(count_evens([1, 22, 4, 33]))