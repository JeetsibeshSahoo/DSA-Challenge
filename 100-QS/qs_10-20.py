# Q-1 -: Two SUM (without built-in use)

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


# Leetcode Optimize one
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

# ++++++++++++++++++++++++++++++++++++++++++++++

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
# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# unique = []
# for i in range(n):
#     if i == 0 or arr[i] != arr[i-1]:
#         unique.append(arr[i])

# print(len(unique))

# for i in range(len(unique)):
#     print(unique[i], end=" ")


# Leetcode optimized one
# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# k = 1

# for i in range(1, len(arr)):
#     if arr[i] != arr[k-1]:
#         arr[k] = arr[i]
#         k += 1

# print(k)
# for i in range(k):
#     print(arr[i], end=" ")

# +++++++++++++++++++++++++++++++++++++++


# Q-4 -: Remove Element

# Without using built-in keyword
# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# val = int(input())
# k = 0

# for i in range(n):
#     if arr[i] != val:
#         arr[k] = arr[i]
#         k += 1

# print(k)

# for i in range(k):
#     print(arr[i], end=" ")




# Using built-in keyword
# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# val = int(input())
# k = 0

# while k < len(arr):
#     if arr[k] == val:
#         arr.pop(k)
#     else:
#         k += 1

# print(k)

# for i in range(k):
#     print(arr[i], end=" ")



#  Leetcode optimized way
# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# val = int(input())

# left = 0
# right = n - 1

# while left <= right:
#     if arr[left] == val:
#         arr[left] = arr[right]
#         right -= 1
#     else:
#         left += 1

# print(left)

# for i in range(left):
#     print(arr[left], end=" ")


# ++++++++++++++++++++

# Q-5 -: Reverse Integer
# Without using built-in keyword.

# x = int(input())

# sign = 1
# if x < 0:
#     sign = -1
#     x = -x


# reverse = 0

# while x != 0:
#     digit = x % 10
#     x = x // 10

#     if reverse > 214748364:
#         print(0)
#         break
#     if reverse == 214748364 and digit > 7:
#         print(0)
#         break

#     reverse = reverse * 10 + digit
# else:
#     reverse = reverse * sign
#     if reverse < -214748364 and reverse > 214748364:
#         print(0)
#     else:
#         print(reverse)


# Using built-in keyword

# x = int(input())

# if x < 0:
#     result = -int(str(-x)[::-1])
# else:
#     result = int(str(x)[::-1])

# if result < -2147483648 or result > 2147483647:
#     print(0)
# else:
#     print(result)


# Optimized version
# x = int(input())

# sign = -1 if x < 0 else 1
# x = abs(x)

# reverse = 0

# while x > 0:
#     digit = x % 10
#     x = x // 10

#     if reverse > (2**31 - 1 - digit) // 10:
#         print(0)

#     reverse = reverse * 10 + digit

# print(sign * reverse)

# +++++++++++++++++++++++++++++++++

# Q-6 -: Find the Index of the First Occurrence in a String
# Without using built-in keyword

# hystack = input()
# needle = input()

# n = len(hystack)
# m = len(needle)

# index = -1

# for i in range(n - m + 1):
#     found = True

#     for j in range(m):
#         if hystack[i + j] != needle[j]:
#             found = False
#             break

#     if found:
#         index = i
#         break

# print(index)


# Using built-in keyword
# hystack = input()
# needle = input()

# index = hystack.find(needle)
# print(index)