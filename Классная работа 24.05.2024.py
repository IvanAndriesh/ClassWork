def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))

# Тесты
print(sum_range(1, 5))  # 15
print(sum_range(5, 1))  # 15
print(sum_range(-3, 4))  # 4
