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