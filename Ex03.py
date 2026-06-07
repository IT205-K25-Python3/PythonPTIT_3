students = [
    {"name": "An", "score": 8.5},
    {"name": "Bình", "score": 6.0},
    {"name": "Chi", "score": 9.0},
    {"name": "Dũng", "score": 5.5}
]

passed_students = [s for s in students if s["score"] >= 8.0]

print("hoc sinh co diem >= 8.0:")
for s in passed_students:
    print(s["name"], ":", s["score"])