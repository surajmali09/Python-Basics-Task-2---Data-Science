def remove_duplicates(data):
    return list(set(data))

def filter_data(data):
    return [x for x in data if x > 10]

raw_data = [5, 12, 7, 12, 18, 5, 25]
print("Raw Data:", raw_data)

cleaned_data = remove_duplicates(raw_data)
print("After Removing Duplicates:", cleaned_data)

filtered_data = filter_data(cleaned_data)
print("After Filtering (>10):", filtered_data)
