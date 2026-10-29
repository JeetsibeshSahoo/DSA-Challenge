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
n = int(input("Enter the number of pairs: "))

result = []

def generate(current, open_count, close_count):
    if len(current) == 2 * n:
        result.append(current)
        return

    if open_count < n:
        generate(current + "(", open_count + 1, close_count)

    if close_count < open_count:
        generate(current + ")", open_count, close_count + 1)

generate("", 0, 0)

for item in result:
    print(item)