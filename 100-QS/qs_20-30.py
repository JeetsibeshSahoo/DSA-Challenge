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


# ++++++++++++++++++++++++++++++++++++

# Q - 7 -: Find First and Last Position of Element in Sorted Array
# Without using built-in keyword

# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# target = int(input())

# # For first occurrence
# left = 0
# right = n - 1
# first = -1

# while left <= right:

#     mid = (left + right) // 2

#     if arr[mid] == target:
#         first = mid
#         right = mid - 1
#     elif arr[mid] < target:
#         left = mid + 1
#     else:
#         left = mid - 1

# # For last occurrence
# left = 0
# right = n - 1
# last = -1

# while left <= right:

#     mid = (left + right) // 2

#     if arr[mid] == target:
#         last = mid
#         left = mid + 1
#     elif arr[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(first, last)

# Using built-in keyword
# from bisect import bisect_left, bisect_right

# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# target = int(input())

# left = bisect_left(arr, target)
# right = bisect_right(arr, target) - 1

# if left == n or arr[left] != target:
#     print(-1, -1)
# else:
#     print(left, right)

# ++++++++++++++++++++++++++++++++++++++++++

# Q-8 -: Longest Substring Without Repeating Characters
# Without using built-in keyword

# s = input()

# max_length = 0

# for i in range(len(s)):

#     current_len = 0

#     for j in range(i, len(s)):

#         duplicate = False

#         for k in range(i, j):
#             if s[k] == s[j]:
#                 duplicate = True
#                 break

#         if duplicate:
#             break

#         current_len += 1

#     if current_len > max_length:
#         max_length = current_len

# print(max_length)


# Using built-in keyword
# s = input()

# seen = set()

# left = 0
# max_length = 0

# for right in range(len(s)):

#     while s[right] in seen:
#         seen.remove(s[left])
#         left += 1

#     seen.add(s[right])

#     curr_len = right - left + 1

#     if curr_len > max_length:
#         max_length = curr_len

# print(max_length)


# Optimized for leetcode
# s = input()

# last = [-1] * 128
# left = 0
# max_length = 0

# for right, char in enumerate(s):
#     index = ord(char)

#     if last[index] >= left:
#         left = last[index] + 1

#     last[index] = right

#     length = right - left + 1

#     if length > max_length:
#         max_length = length

# print(max_length)

# +++++++++++++++++++++++++++++++++++++
# Q-9 -: Power of Two
# Without using built-in keyword

# n = int(input())

# if n <= 0:
#     print("False")
# else:
#     while n % 2 == 0:
#         n = n // 2

#     if n == 1:
#         print("True")
#     else:
#         print("False")


# Using built-in keyword
# n = int(input())

# if n > 0 and bin(n).count("1") == 1:
#     print("True")
# else:
#     print("False")

# +++++++++++++++++++++++++++++++++++++++++++

# Q - 10 -: Roman to Integer
# Without using built-in keyword

# s = input().strip()

# total = 0

# for i in range(len(s)):
#     if s[i] == "I":
#         current = 1
#     elif s[i] == "V":
#         current = 5
#     elif s[i] == "X":
#         current = 10
#     elif s[i] == 'L':
#         current = 50
#     elif s[i] == 'C':
#         current = 100
#     elif s[i] == 'D':
#         current = 500
#     else:
#         current = 1000

#     if i + 1 < len(s):
#         if s[i + 1] == "I":
#             next_value = 1
#         elif s[i + 1] == 'V':
#             next_value = 5
#         elif s[i + 1] == 'X':
#             next_value = 10
#         elif s[i + 1] == 'L':
#             next_value = 50
#         elif s[i + 1] == 'C':
#             next_value = 100
#         elif s[i + 1] == 'D':
#             next_value = 500
#         else:
#             next_value = 1000

#     else:
#         next_value = 0

#     if current < next_value:
#         total = total - current
#     else:
#         total = total + current

# print(total)

# Using built-in keyword
s = input().strip()

values = {
    "I" : 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

total = 0

for i in range(len(s)):
    if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
        total = total - values[s[i]]
    else:
        total = total + values[s[i]]

print(total)




# Q-11 -: Longest Common Prefix

# Without using built-in keyword
# n = int(input())

# strs = []
# for i in range(n):
#     strs.append(input().strip())

# if n == 0:
#     print("")
# else:
#     common_length = 0

#     for i in range(len(strs[0])):

#         curr_char = strs[0][i]
#         matches = True

#         for j in range(1, n):

#             if i >= len(strs[j]) or strs[j][i] != curr_char:
#                 matches = False
#                 break

#         if not matches:
#             break

#         common_length += 1

#     print(strs[0][:common_length])


# Using built-in keyword
# n = int(input())

# strs = []
# for i in range(n):
#     strs.append(input().strip())

# if n == 0:
#     print("")
# else:

#     strs.sort()

#     first = strs[0]
#     last = strs[n - 1]

#     i = 0

#     while i < len(first) and i < len(last) and first[i] == last[i]:
#         i += 1

#     print(first[:i])


# Optimized code for LeetCode
# n = int(input())

# strs = []
# for i in range(n):
#     strs.append(input().strip())

# if n == 0:
#     print("")
# else:
#     prefix = strs[0]

#     for i in range(1, n):
#         word = strs[i]
#         j = 0

#         while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
#             j += 1

#         prefix = prefix[:j]

#         if not prefix:
#             print("")

#     print(prefix)


# ++++++++++++++++++++++++++++++++++++++++++++=

# Q-12 -: Container With Most Water
# Without using built-in keyword

# n = int(input("Enter the number of heights: "))

# height = list(map(int, input("Enter the heights: ").split()))

# left = 0
# right = n - 1
# max_area = 0

# while left < right:
#     width = right - left

#     if height[left] < height[right]:
#         shorter_height = height[left]
#     else:
#         shorter_height = height[right]

#     current_area = shorter_height * width

#     if current_area > max_area:
#         max_area = current_area

#     if height[left] < height[right]:
#         left += 1
#     else:
#         right -= 1

# print(max_area)



# Using built-in keyword
# n = int(input("Enter the number of heights: "))

# height = list(map(int, input("Enter the heights: ").split()))

# left = 0
# right = n - 1
# max_area = 0

# while left < right:

#     width = right - left

#     current_area = min(height[left], height[right]) * width

#     max_area = max(max_area, current_area)

#     if height[left] < height[right]:
#         left += 1
#     else:
#         right -= 1

# print(max_area)


# Optimized code for leetcode

# n = int(input("Enter the number of heights: "))

# height = list(map(int, input("Enter the heights: ").split()))

# left = 0
# right = n - 1
# max_water = 0

# while left < right:
#     width = right - left

#     if height[left] < height[right]:
#         area = height[left] * width
#         left += 1
#     else:
#         area = height[right] * width
#         right -= 1

#     if area > max_water:
#         max_water = area

# print(max_water)


# ++++++++++++++++++++++++++++++

# Q-13 -: Length of Last Word
# Without using built-in keyword

# s = input()

# i = len(s) - 1
# length = 0

# while i >= 0 and s[i] == " ":
#     i -= 1

# while i >= 0 and s[i] != " ":
#     length += 1
#     i -= 1

# print(length) 


# Using built-in keyword
# s = input()

# words = s.split()

# if len(words) == 0:
#     print(0)
# else:
#     print(len(words[-1]))


# Optimized code for LeetCode
# s = input()

# i = len(s) - 1

# while s[i] == ' ':
#     i -= 1

# length = 0

# while i >= 0 and s[i] != ' ':
#     length += 1
#     i -= 1

# print(length)

# +++++++++++++++++++++++++++++++++++++

# Q-14 -: Longest Palindromic Substring
# Without using built-in keyword

# s = input("Enter the string: ")

# n = len(s)
# start = 0
# max_len = 0

# for i in range(n):

#     left = i
#     right = i

#     while left >= 0 and right < n and s[left] == s[right]:

#         curr_len = right - left + 1

#         if curr_len > max_len:
#             max_len = curr_len
#             start = left

#         left -= 1
#         right += 1

#     left = i
#     right = i + 1

#     while left >= 0 and right < n and s[left] == s[right]:
    
#         curr_len = right - left + 1
    
#         if curr_len > max_len:
#             max_len = curr_len
#             start = left
    
#         left -= 1
#         right += 1

# print(s[start:start + max_len])


# Using built-in keyword
# s = input("Enter the string: ")

# n = len(s)
# longest = ""

# for length in range(n, 0, -1):

#     found = False

#     for start in range(n - length + 1):

#         substring = s[start:start + length]

#         if substring == substring[::-1]:
#             longest = substring
#             found = True
#             break

#         if found:
#             break

#     print(longest)

# Optimized code for Leetcode
# s = input("Enter the string: ")


# start = 0
# max_len = 1

# for i in range(len(s)):
#     left = i
#     right = i

#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1

#     length = right - left - 1

#     if length > max_len:
#         max_len = length
#         start = left + 1

#     left = i
#     right = i + 1

#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1

#     length = right - left - 1

#     if length > max_len:
#         max_len = length
#         start = left + 1

# print(s[start:start + max_len])

# +++++++++++++++++++++++++++++++++++++

# Q-15 -: Search Insert Position
# Without using built-in keyword
# n = int(input("Enter the length of the array: "))

# nums = list(map(int, input("Enter array elements: ").split()))

# target = int(input("Enter the target: "))

# left = 0
# right = n

# while left < right:

#     mid = left + (right - left) // 2

#     if nums[mid] < target:
#         left = mid + 1
#     else:
#         right = mid

# print(left)


# Using built-in keyword
# from bisect import bisect_left

# n = int(input("Enter the length of the array: "))

# nums = list(map(int, input("Enter array elements: ").split()))

# target = int(input("Enter the target: "))

# print(bisect_left(nums, target))



# Optimized code for leetcode
n = int(input("Enter the length of the array: "))

nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter the target: "))

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print(mid)
        break

    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1



# ++++++++++ 383 +++++++++++++++++++++++++
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


# ++++++++++++++++++++++++++++++++++++

# Q - 7 -: Find First and Last Position of Element in Sorted Array
# Without using built-in keyword

# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# target = int(input())

# # For first occurrence
# left = 0
# right = n - 1
# first = -1

# while left <= right:

#     mid = (left + right) // 2

#     if arr[mid] == target:
#         first = mid
#         right = mid - 1
#     elif arr[mid] < target:
#         left = mid + 1
#     else:
#         left = mid - 1

# # For last occurrence
# left = 0
# right = n - 1
# last = -1

# while left <= right:

#     mid = (left + right) // 2

#     if arr[mid] == target:
#         last = mid
#         left = mid + 1
#     elif arr[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(first, last)

# Using built-in keyword
# from bisect import bisect_left, bisect_right

# n = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

# target = int(input())

# left = bisect_left(arr, target)
# right = bisect_right(arr, target) - 1

# if left == n or arr[left] != target:
#     print(-1, -1)
# else:
#     print(left, right)

# ++++++++++++++++++++++++++++++++++++++++++

# Q-8 -: Longest Substring Without Repeating Characters
# Without using built-in keyword

# s = input()

# max_length = 0

# for i in range(len(s)):

#     current_len = 0

#     for j in range(i, len(s)):

#         duplicate = False

#         for k in range(i, j):
#             if s[k] == s[j]:
#                 duplicate = True
#                 break

#         if duplicate:
#             break

#         current_len += 1

#     if current_len > max_length:
#         max_length = current_len

# print(max_length)


# Using built-in keyword
# s = input()

# seen = set()

# left = 0
# max_length = 0

# for right in range(len(s)):

#     while s[right] in seen:
#         seen.remove(s[left])
#         left += 1

#     seen.add(s[right])

#     curr_len = right - left + 1

#     if curr_len > max_length:
#         max_length = curr_len

# print(max_length)


# Optimized for leetcode
# s = input()

# last = [-1] * 128
# left = 0
# max_length = 0

# for right, char in enumerate(s):
#     index = ord(char)

#     if last[index] >= left:
#         left = last[index] + 1

#     last[index] = right

#     length = right - left + 1

#     if length > max_length:
#         max_length = length

# print(max_length)

# +++++++++++++++++++++++++++++++++++++
# Q-9 -: Power of Two
# Without using built-in keyword

# n = int(input())

# if n <= 0:
#     print("False")
# else:
#     while n % 2 == 0:
#         n = n // 2

#     if n == 1:
#         print("True")
#     else:
#         print("False")


# Using built-in keyword
# n = int(input())

# if n > 0 and bin(n).count("1") == 1:
#     print("True")
# else:
#     print("False")

# +++++++++++++++++++++++++++++++++++++++++++

# Q - 10 -: Roman to Integer
# Without using built-in keyword

# s = input().strip()

# total = 0

# for i in range(len(s)):
#     if s[i] == "I":
#         current = 1
#     elif s[i] == "V":
#         current = 5
#     elif s[i] == "X":
#         current = 10
#     elif s[i] == 'L':
#         current = 50
#     elif s[i] == 'C':
#         current = 100
#     elif s[i] == 'D':
#         current = 500
#     else:
#         current = 1000

#     if i + 1 < len(s):
#         if s[i + 1] == "I":
#             next_value = 1
#         elif s[i + 1] == 'V':
#             next_value = 5
#         elif s[i + 1] == 'X':
#             next_value = 10
#         elif s[i + 1] == 'L':
#             next_value = 50
#         elif s[i + 1] == 'C':
#             next_value = 100
#         elif s[i + 1] == 'D':
#             next_value = 500
#         else:
#             next_value = 1000

#     else:
#         next_value = 0

#     if current < next_value:
#         total = total - current
#     else:
#         total = total + current

# print(total)

# Using built-in keyword
s = input().strip()

values = {
    "I" : 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

total = 0

for i in range(len(s)):
    if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
        total = total - values[s[i]]
    else:
        total = total + values[s[i]]

print(total)