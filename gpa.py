# A program that calculates the GPA of a KTH student based on a list of courses and grades.
# Author: Isak Einberg

# Map grades to their value in accordance to the KTH GPA scale
grade_value = {
    'A': 5.0,
    'B': 4.5,
    'C': 4.0,
    'D': 3.5,
    'E': 3.0,
    'F': 0.0
}

# Courses are provided as a list of tuples containing the course name, credits (hp) and grade respectively
grades = [
    ("course 2", 3.0, 'B'),
    ("Course 3", 3.0, 'F'),
    ("Example 1", 7.5, 'A'),
    ("Course 4", 12.5, 'B'),
    ("Example 2", 3.0, 'D'),
    ("Course 1", 4.5, 'D'),
    ("Example 3", 7.5, 'A'),
    ("sample course", 6.0, 'C'),
    ("Test course", 10.5, 'A')
]

# Initialize a dictionary with 0 occurrences of each grade
occurences_of_grade = {k: 0 for k in grade_value.keys()}

# Calculate GPA
total_hp = 0.0
points = 0.0
for _, hp, grade in grades:
    total_hp += hp
    points += hp * grade_value[grade]
    occurences_of_grade[grade] += 1
gpa = points / total_hp

# Sort courses by grade and course name
grades.sort(key=lambda x: x[0].lower())
grades.sort(key=lambda x: x[2])

# Adjust column width to fit longest course name
course_column_width = 1 + max(len(course) for course, _, _ in grades)
print("\nCourses:")
for course, hp, grade in grades:
    print(f"\t{course:{course_column_width}} {grade} {hp:5} hp")


summary = "\nSummary:\n\t"
for grade in grade_value.keys():
    if occurences_of_grade[grade] == 0:
        continue
    suffix = ',' if grade != 'F' else '\n'
    summary += f"{grade}: {occurences_of_grade[grade]}x{suffix:3}"
print(summary)

# Current GPA
print("GPA: %.2f" % gpa + "\n")
