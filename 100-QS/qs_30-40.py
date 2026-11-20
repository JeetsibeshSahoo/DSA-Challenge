# Q-31 -: Spiral Matrix
# Without using built-in keyword
# def spiralOrder(matrix):
#     result = []

#     top = 0
#     bottom = len(matrix) - 1
#     left = 0
#     right = len(matrix[0]) - 1

#     while top <= bottom and left <= right:

#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1

#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1

#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[bottom][i])
#             bottom -= 1

#         if left < right:
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1

#     return result

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# print("Enter matrix elements row by row:")

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# result = spiralOrder(matrix)

# print("Spiral order:", result)



# Using built-in keyword
# def spiralOrder(matrix):
#     result = []

#     while matrix:
#         result += matrix.pop(0)

#         if matrix and matrix[0]:
#             for row in matrix:
#                 result.append(row.pop())

#         if matrix:
#             result += matrix.pop()[::-1]

#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 result.append(row.pop(0))

#     return result

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# print("Enter matrix elements row by row:")

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# result = spiralOrder(matrix)

# print("Spiral order:", result)


# +++++++++++++++++++++++++++++++++++++++++++++++
# Q-32 -: Spiral Matrix II
# Without using built-in keyword
# def generateMatrix(n):
#     matrix = [[0] * n for _ in range(n)]

#     top = 0
#     bottom = n - 1
#     left = 0
#     right = n - 1

#     num = 1

#     while top <= bottom and left <= right:

#         for i in range(left, right + 1):
#             matrix[left][i] = num
#             num += 1
#         top += 1

#         for i in range(top, bottom + 1):
#             matrix[i][right] = num
#             num += 1
#         right -= 1

#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 matrix[bottom][i] = num
#                 num += 1
#             bottom -= 1

#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 matrix[i][left] = num
#                 num += 1
#             left += 1

#     return matrix

# n = int(input("Enter the value of n: "))

# result = generateMatrix(n)

# print("Spiral Matrix: ")

# for row in result:
#     print(*row)



# Another way
# def generateMatrix(n):
#     nums = list(range(1, n * n + 1))
#     matrix = [[0] * n for _ in range(n)]

#     top = 0
#     bottom = n - 1
#     left = 0
#     right = n - 1

#     while nums:

#         for j in range(left, right + 1):
#             matrix[top][j] = nums.pop(0)
#         top += 1

#         for i in range(top, bottom + 1):
#             matrix[i][right] = nums.pop(0)
#         right -= 1

#         if top <= bottom:
#             for j in range(right, left - 1, -1):
#                 matrix[bottom][j] = nums.pop(0)
#             bottom -= 1

#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 matrix[i][left] = nums.pop(0)
#             left += 1

#     return matrix


# n = int(input("Enter the value of n: "))

# result = generateMatrix(n)

# print("Spiral Matrix: ")

# for row in result:
#     print(*row)


# +++++++++++++++++++++++++++++++++++++++++++++++++
# Q-33 -: Regular Expression Matching
# Without using built-in keyword
# def isMatch(s, p):
#     m = len(s) 
#     n = len(p)

#     dp = [[False] * (n + 1) for _ in range(m + 1)]

#     dp[0][0] = True

#     for j in range(2, n + 1):
#         if p[j - 1] == '*':
#             dp[0][j] = dp[0][j - 2]

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):

#             if p[j - 1] == "." or p[j - 1] == s[i - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]

#             elif p[j - 1] == "*":
#                 dp[i][j] = dp[i][j - 2]

#                 if p[j - 2] == "." or p[j - 2] == s[i - 1]:
#                     dp[i][j] = dp[i][j] or dp[i - 1][j]

#     return dp[m][n]

# s = input("Enter the strings: ")
# p = input("Enter the pattern: ")

# result = isMatch(s, p)

# print(result)


# Using built-in keyword
# import re

# def isMatch(s, p):
#     return re.fullmatch(p, s) is not None

# s = input("Enter the string: ")
# p = input("Enter the pattern: ")

# result = isMatch(s, p)

# print(result)


# +++++++++++++++++++++++++++++++++++++++++++
# Q-34 -: Sqrt(x)
# Without using built-in keyword
# def mySqrt(x):

#     if x < 2:
#         return x

#     left = 1
#     right = x // 2
#     answer = 0

#     while left <= right:

#         mid = left + (right - left) // 2

#         if mid <= x // mid:
#             answer = mid
#             left = mid + 1

#         else:
#             right = mid - 1

#     return answer

# x = int(input("Enter the number: "))

# result = mySqrt(x)

# print(result)


# Using built-in keyword
import math

def mySqrt(x):
    return math.isqrt(x)

x = int(input("Enter the number: "))

result = mySqrt(x)

print(result)
