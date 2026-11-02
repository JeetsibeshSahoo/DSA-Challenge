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