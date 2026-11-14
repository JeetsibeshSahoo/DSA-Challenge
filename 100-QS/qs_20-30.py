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


# Using built-in keyword
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

# ++++++++++++++++++++++++++++++++++++++++
# Q-28 -: Median of Two Sorted Array
# Without using built-in keyword (Approach 1)
# def findMedianSortedArrays(nums1, nums2):
#     i = 0
#     j = 0
#     arr = []

#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             arr.append(nums1[i])
#             i += 1
#         else:
#             arr.append(nums2[j])
#             j += 1

#     arr.extend(nums1[i:])
#     arr.extend(nums2[j:])

#     n = len(arr)

#     if n % 2 == 1:
#         return arr[n // 2]

#     return (arr[n // 2 - 1] + arr[n // 2]) / 2


# nums1 = list(map(int, input("Enter first sorted array: ").split()))
# nums2 = list(map(int, input("Enter second sorted array: ").split()))

# result = findMedianSortedArrays(nums1, nums2)

# print("Median:", result)



# Without using built-in keyword (Approach 2 - Binary Search )
# def findMedianSortedArrays(nums1, nums2):

#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1

#     m = len(nums1)
#     n = len(nums2)

#     low = 0
#     high = m

#     while low <= high:

#         i = (low + high) // 2
#         j = (m + n + 1) // 2 - i

#         left1 = float('-inf') if i == 0 else nums1[i - 1]
#         right1 = float('inf') if i == m else nums1[i]

#         left2 = float('-inf') if j == 0 else nums2[j - 1]
#         right2 = float('inf') if j == n else nums2[j]

#         if left1 <= right2 and left2 <= right1:

#             if (m + n) % 2 == 1:
#                 return float(max(left1, left2))

#             return (max(left1, left2) + min(right1, right2)) / 2.0

#         elif left1 > right2:
#             high = i - 1

#         else:
#             low = i + 1

# nums1 = list(map(int, input("Enter first sorted array: ").split()))
# nums2 = list(map(int, input("Enter second sorted array: ").split()))

# result = findMedianSortedArrays(nums1, nums2)

# print("Median:", result)


# Using built-in keyword
# def findMedianSortedArrays(nums1, nums2):
#     arr = sorted(nums1 + nums2)

#     n = len(arr)

#     if n % 2 == 1:
#         return arr[n // 2]

#     return (arr[n // 2 - 1] + arr[n // 2]) / 2


# nums1 = list(map(int, input("Enter first sorted array: ").split()))
# nums2 = list(map(int, input("Enter second sorted array: ").split()))

# result = findMedianSortedArrays(nums1, nums2)

# print("Median:", result)
