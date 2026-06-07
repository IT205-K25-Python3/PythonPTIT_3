students = [
    {"name": "An", "score": 8},
    {"name": "Binh", "score": 7},
    {"name": "Chi", "score": 9}
]

for student in students:
    print(f"ten: {student['name']}, diem: {student['score']}")

total = sum(student["score"] for student in students)
average = total / len(students)
print(f"diem trung binh: {average}")


top_student = max(students, key=lambda x: x["score"])
print(f"hoc sinh co diem cao nhat: {top_student['name']}")
