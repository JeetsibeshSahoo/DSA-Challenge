#  Two SUM (without built-in use)

# n = int(input())

# arr = []  # arr = [1,4,4,5,7]
# for i in range(n):
#     arr.append(int(input()))

# target = int(input())

# found = False

# for i in range(n):
#     for j in range(i+1, n):
#         if arr[i] + arr[j] == target:
#             print(i, j)
#             found = True
#             break

#     if found:
#         break



# Two SUM (using built-in keyword)
# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# target = int(input())

# seen = {}

# for i in range(n):
#     required = target - arr[i]

#     if required in seen:
#         print(seen[required], i)
#         break

#     seen[arr[i]] = i

# +++++++++++++++++++++++++++++++++++++++++++++

# Q-2 -: Palindrome Number -: Given an integer x, return true if x is a palindrome, and false otherwise. (without built-in use)

# x = int(input())

# if x < 0:
#     print("False")
# else:
#     original = x
#     reversed = 0

#     while x > 0:
#         digit = x % 10
#         reversed = reversed * 10 + digit
#         x = x // 10

#     if original == reversed:
#         print("True")
#     else:
#         print("False")


# Using Built-in keyword

# x = int(input())

# if x < 0:
#     print("False")
# else:
#     s = str(x)
#     if s == s[::-1]:
#         print("True")
#     else:
#         print("False")


# More Optimize one
# x = int(input())

# if x < 0:
#     print("False")

# if x % 10 == 0 and x != 0:
#     print("False")

# reversed_half = 0

# while x > reversed_half:
#     reversed_half = reversed_half * 10 + x % 10
#     x //= 10
# if x == reversed_half or x == reversed_half // 10:
#     print("True")


# Q-3 -: Remove Duplicates from Sorted Array (Without using Built-in keyword)

# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# if n == 0:
#     print(0)
# else :
#     k = 1
#     for i in range(1, n):
#         if arr[i] != arr[k-1]:
#             arr[k] = arr[i]
#             k += 1
#     print(k)

#     for i in range(k):
#         print(arr[i], end=" ")

# Using Built-in keyword
n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

unique = []
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        unique.append(arr[i])

print(len(unique))

for i in range(len(unique)):
    print(unique[i], end=" ")