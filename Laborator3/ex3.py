def normalize_data(data):
    if not data:
        return []

    min_val = min(data)
    max_val = max(data)

    if max_val == min_val:
        return [0 for _ in data]

    normalized = []

    for x in data:
        norm = (x - min_val) / (max_val - min_val)
        normalized.append(norm)

    return normalized

data = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data)

print(normalized_data)