# Q-21 -: Generate Parentheses
# Without using built-in keyword

# n = int(input("Enter the number of pairs: "))

# result = []
# path = []

# def generate(open_count, close_count):

#     if len(path) == 2 * n:
#         result.append("".join(path))

#     if open_count < n:
#         path.append("(")
#         generate(open_count + 1, close_count)
#         path.pop()

#     if close_count < open_count:
#         path.append(")")
#         generate(open_count, close_count + 1)
#         path.pop()

# generate(0, 0)

# for item in result:
#     print(item)


# Using built-in keyword
# n = int(input("Enter the number of pairs: "))

# result = []

# def generate(current, open_count, close_count):
#     if len(current) == 2 * n:
#         result.append(current)
#         return

#     if open_count < n:
#         generate(current + "(", open_count + 1, close_count)

#     if close_count < open_count:
#         generate(current + ")", open_count, close_count + 1)

# generate("", 0, 0)

# for item in result:
#     print(item)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Q-22 -: Add Binary
# Without using built-in keyword

# a = input("Enter First Number: ").strip()
# b = input("Enter Second Number: ").strip()

# i = len(a) - 1
# j = len(b) - 1

# carry = 0
# result = []

# while i >= 0 or j >= 0 or carry > 0:

#     total = carry

#     if i >= 0:
#         total += int(a[i])
#         i -= 1

#     if j >= 0:
#         total += int(b[j])
#         j -= 1

#     result.append(str(total % 2))
#     carry = total // 2

# answer = "".join(reversed(result))

# print(answer)


# Using built-in keyword
# a = input("Enter First Number: ").strip()
# b = input("Enter Second Number: ").strip()

# num1 = int(a, 2)
# num2 = int(b, 2)

# total = num1 + num2

# result = bin(total)[2:]

# print(result)


# ++++++++++++++++++++++++++++++++++++++++

# Q-23 -: Letter Combinations of a Phone Number
# Without using built-in keyword
# digits = input("Enter digits: ").strip()

# phone = {
#     '2': 'abc',
#     '3': 'def',
#     '4': 'ghi',
#     '5': 'jkl',
#     '6': 'mno',
#     '7': 'pqrs',
#     '8': 'tuv',
#     '9': 'wxyz'
# }

# result = []
# current = []

# def backtrack(index):

#     if index == len(digits):
#         result.append("".join(current))
#         return

#     letters = phone[digits[index]]

#     for i in range(len(letters)):
#         current.append(letters[i])
#         backtrack(index + 1)
#         current.pop()

# if digits:
#     backtrack(0)

# for combination in result:
#     print(combination)


# Using built-in keyword
# from itertools import product

# digits = input("Enter digits: ").strip()

# phone = {
#     '2': 'abc',
#     '3': 'def',
#     '4': 'ghi',
#     '5': 'jkl',
#     '6': 'mno',
#     '7': 'pqrs',
#     '8': 'tuv',
#     '9': 'wxyz'
# }

# if digits:
#     letter_groups = []

#     for digit in digits:
#         letter_groups.append(phone[digit])

#     combinations = product(*letter_groups)

#     for combination in combinations:
#         print("".join(combination))


# Optimized code for Leetcode
# digits = input("Enter digits: ").strip()

# if not digits:
#     print("")

# mapping = (
#     "", "", "abc", "def", "ghi",
#     "jkl", "mno", "pqrs", "tuv", "wxyz"
# )

# result = []
# path = []
# n = len(digits)

# def backtrack(index):
#     if index == n:
#         result.append("".join(path))
#         return

#     for char in mapping[ord(digits[index]) - 48]:
#         path.append(char)
#         backtrack(index + 1)
#         path.pop()

# backtrack(0)
# print(result)

# ++++++++++++++++++++++++++++++++++++++++

# Q-24 -: Rotate Image
# Without using built-in keyword
# def rotate(matrix):
#     n = len(matrix)

#     for i in range(n):
#         for j in range(i + 1, n):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp

#     for i in range(n):
#         left = 0
#         right = n - 1

#         while left < right:
#             temp = matrix[i][left]
#             matrix[i][left] = matrix[i][right]
#             matrix[i][right] = temp

#             left += 1
#             right -= 1


# n = int(input("Enter matrix size: "))

# matrix = []

# print("Enter matrix rows:")
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# rotate(matrix)

# print("Rotated matrix:")
# for row in matrix:
#     print(*row)


# Using built-in keyword
# def rotate(matrix):
#     n = len(matrix)

#     for i in range(n):
#         for j in range(i + 1, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     for row in matrix:
#         row.reverse()

#     return matrix

# n = int(input("Enter matrix size: "))

# matrix = []

# print("Enter matrix rows:")
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# rotate(matrix)

# print("Rotated matrix:")
# for row in matrix:
#     print(*row)


# +++++++++++++++++++++++++++++++++++++++++++
# Q-25 -: Combination Sum
# Without using built-in keyword
# def combinationSum(candidates, target):

#     result = []
#     current = []

#     candidates.sort()

#     def findCombinations(index, total):

#         if total == target:
#             result.append(current.copy())
#             return

#         if total > target:
#             return

#         for i in range(index, len(candidates)):

#             current.append(candidates[i])
#             findCombinations(i, total + candidates[i])
#             current.pop()

#     findCombinations(0, 0)

#     return result

# n = int(input("Enter number of candidates: "))

# candidates = list(map(int, input("Enter candidates: ").split()))

# target = int(input("Enter target: "))

# result = combinationSum(candidates, target)

# print("Combinations: ")
# print(result)


# Using built-in keyword
# def combinationSum(candidates, target):
#     result = []

#     candidates.sort()

#     def backtrack(start, current, total):
#         if total == target:
#             result.append(current[:])
#             return

#         if total > target:
#             return

#         for i in range(start, len(candidates)):
#             current.append(candidates[i])

#             backtrack(i, current, total + candidates[i])

#             current.pop()

#     backtrack(0, [], 0)

#     return result


# n = int(input("Enter number of candidates: "))

# candidates = list(map(int, input("Enter candidates: ").split()))

# target = int(input("Enter target: "))

# result = combinationSum(candidates, target)

# print("Output:")
# print(result)


# ++++++++++++++++++++++++++++++++++++++++++++++++
# Q-25 -: Combination Sum II
# def combinationSum2(candidates, target):
#     result = []
#     current = []

#     candidates.sort()

#     def findCombinations(index, total):

#         if total == target:
#             result.append(current.copy())
#             return

#         if total > target:
#             return

#         for i in range(index, len(candidates)):

#             if i > index and candidates[i] == candidates[i - 1]:
#                 continue

#             current.append(candidates[i])

#             findCombinations(i + 1, total + candidates[i])

#             current.pop()

#     findCombinations(0, 0)

#     return result

# n = int(input("Enter number of candidates: "))

# candidates = list(map(int, input("Enter candidates: ").split()))

# target = int(input("Enter target: "))

# result = combinationSum2(candidates, target)

# print("Combinations: ")
# print(result)


# ++++++++++++++++++++++++++++++++++++++++++++++++
# Q-27 -: Permutations
# Without using built-in keyword
# def permute(nums):
#     result = []
#     current = []
#     used = [False] * len(nums)

#     def backtrack():

#         if len(current) == len(nums):
#             result.append(current.copy())
#             return

#         for i in range(len(nums)):

#             if used[i]:
#                 continue

#             current.append(nums[i])
#             used[i] = True

#             backtrack()

#             current.pop()
#             used[i] = False

#     backtrack()

#     return result


# n = int(input("Enter number of elements: "))
# nums = list(map(int, input("Enter elements: ").split()))
# result = permute(nums)

# print("Permutations:")
# print(result)


# Using builtin keyword
# from itertools import permutations

# def permute(nums):
#     result = []

#     for p in permutations(nums):
#         result.append(list(p))

#     return result


# nums = list(map(int, input("Enter elements: ").split()))
# print(permute(nums))


# Optimized code for Leetcode
# def permute(nums):
#     ans = []
#     n = len(nums)

#     def backtrack(i):
#         if i == n:
#             ans.append(nums[:])
#             return

#         for j in range(i, n):
#             nums[i], nums[j] = nums[j], nums[i]
#             backtrack(i + 1)
#             nums[i], nums[j] = nums[j], nums[i]

#     backtrack(0)
#     return ans

# n = int(input("Enter number of elements: "))
# nums = list(map(int, input("Enter elements: ").split()))
# result = permute(nums)

# print("Permutations:")
# print(result)







# +++++++++++++++++++++++++++++++++++++++++++++++++++++

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