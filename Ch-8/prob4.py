def sum(n):
    if n ==1:
        return 1
    return sum(n-1) + n

print(sum(4))

# sum(4)
#  → sum(3) + 4
#     → sum(2) + 3 + 4
#         → sum(1) + 2 + 3 + 4
#             → 1 + 2 + 3 + 4
# = 10
