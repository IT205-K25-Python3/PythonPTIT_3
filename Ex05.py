students = [
    {"name": "An", "class": "Python01"},
    {"name": "Binh", "class": "Python02"},
    {"name": "Chi", "class": "Python01"},
    {"name": "Dung", "class": "Python03"},
    {"name": "Ha", "class": "Python02"}
]

class_count = {}
for student in students:
    course = student["class"]
    if course in class_count:
        class_count[course] += 1
    else:
        class_count[course] = 1

print(class_count)