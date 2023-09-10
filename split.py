def split(items, ratios):
    total_elements = len(items)
    total_ratio = sum(ratios)
    result = []

    start = 0
    for ratio in ratios:
        count = round(total_elements * ratio / total_ratio)
        end = start + count

        result.append(items[start:end])
        start = end

    return result


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ratios = [0.7, 0.2, 0.1]
result = split(items, ratios)
print(result)

