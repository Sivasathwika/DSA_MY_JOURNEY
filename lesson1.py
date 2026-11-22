# LESSON 1.1
#1. Modulo(%) and Integer division(//)
print("Modulo:",7 % 3)
print("division:",7 // 3)

#2. GCD
# euclidean algorithm
# GCD(a,b) = GCD(b, a%b). until b==0

def gcde(a,b):
    while b:
        a, b = b, a % b
    return a

print("euclidean gcd:",gcde(4, 24))

# builtin
import math
print("built-in:", math.gcd(4, 24))

#3. Prime Numbers
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("is prime or not:",is_prime(23))

#4. Bit Maanipulation
x = 20
if x & 1 == 1:
    print("Odd")
else:
    print("Even")

#DRILL
# math way
def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2

    return n == 1

print("math way:",is_power_of_two(16))

# bitwise way
def is_power_two_bit(n):
    if n <= 0:
        return False
    return (n & (n -1)) == 0

print("bitwise way:", is_power_two_bit(16))





