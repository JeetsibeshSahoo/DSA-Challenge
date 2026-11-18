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
def generateMatrix(n):
    nums = list(range(1, n * n + 1))
    matrix = [[0] * n for _ in range(n)]

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while nums:

        for j in range(left, right + 1):
            matrix[top][j] = nums.pop(0)
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = nums.pop(0)
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = nums.pop(0)
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = nums.pop(0)
            left += 1

    return matrix


n = int(input("Enter the value of n: "))

result = generateMatrix(n)

print("Spiral Matrix: ")

for row in result:
    print(*row)