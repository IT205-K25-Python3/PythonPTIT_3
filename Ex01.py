students = [
    {"name": "An", "score": 8},
    {"name": "Binh", "score": 7},
    {"name": "Chi", "score": 9}
]

max_score = max(student["score"] for student in students)
print(f"diem cao nhat: {max_score}")

top_students = [student for student in students if student["score"] == max_score]

print("hoc sinh co diem cao nhat:")
for student in top_students:
    print(f"{student['name']}: {student['score']}")