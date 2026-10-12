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
n = int(input())

strs = []
for i in range(n):
    strs.append(input().strip())

if n == 0:
    print("")
else:
    prefix = strs[0]

    for i in range(1, n):
        word = strs[i]
        j = 0

        while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
            j += 1

        prefix = prefix[:j]

        if not prefix:
            print("")

    print(prefix)