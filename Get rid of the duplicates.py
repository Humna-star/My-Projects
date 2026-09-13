student_data = {
    "id1": {"name": "Alice","class": "VI","subject-integration": ["Math", "Science", "English"],},
    "id2": {"name": "Bob","class": "VI","subject-integration": ["Math", "History", "Geography"]},
    "id3": {"name": "Alice","class": "VI","subject-integration": ["Math", "Science", "English"]},
    "id4": {"name": "Charlie","class": "VII","subject-integration": ["Math", "Science", "English"]},
}

result = {}
seen_keys = []

for student_id, student_info in student_data.items():
    unique_key = (student_info["name"], student_info["class"], tuple(student_info["subject-integration"]))

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = student_info

for k, v in result.items():
    print(k,":", v)