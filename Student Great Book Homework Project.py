
# 1. Dictionary created with at least 5 student name-score pairs (5 marks)
grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 64,
    "Rose": 24,
    "Frances": 12
}

# 2. A loop correctly calculates and prints the class average (10 marks)
total_score = 0
for student in grade_book:
    total_score += grade_book[student]

class_average = total_score / len(grade_book)
print(f"Class Average Score: {class_average:.2f}")
print("-" * 40)

# 3. Highest and lowest scores and students identified (10 marks)
# Using max() and min() with a key to find the student names based on scores
top_student = max(grade_book, key=grade_book.get)
top_score = grade_book[top_student]

bottom_student = min(grade_book, key=grade_book.get)
bottom_score = grade_book[bottom_student]

print(f"Top Scorer: {top_student} with a score of {top_score}")
print(f"Bottom Scorer: {bottom_student} with a score of {bottom_score}")
print("-" * 40)

# 4. .get() used to look up student with a friendly message if missing (10 marks)
# 5. Program runs without any errors (5 marks)
search_name = input("Enter the student's name to look up their grade: ").strip()

# Using .get() with a default 'None' fallback to check if student exists
student_grade = grade_book.get(search_name)

if student_grade is not None:
    print(f"Found it! {search_name}'s score is {student_grade}.")
else:
    print(f"Sorry, '{search_name}' is not registered in this grade book.")