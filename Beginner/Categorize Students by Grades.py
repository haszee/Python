grades = {
    "Alice": 78,
    "Bob": 42,
    "Charlie": 65,
    "Diana": 49,
    "Eve": 90
}

categories = {}

for name in grades.keys():
    if grades[name] < 50:
        categories[name] = 'Fail'
    elif grades[name] >= 50 & grades[name] < 70:
        categories[name] = 'Low Pass'
    elif grades[name] >= 70 & grades[name] < 85:
        categories[name] = 'Pass'
    else:
        categories[name] = 'High Pass'

print(f"Student Categories:\nless than 50%: Fail\n50-69%: Low Pass\n70-84%: Pass\n>=85%: High Pass\n")


print(f"{'\n'.join(f"{key}: {value}" for key,value in categories.items())}")

