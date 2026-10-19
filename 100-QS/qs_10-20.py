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