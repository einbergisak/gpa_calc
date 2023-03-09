# KTH GPA calculator
Simple GPA calculator for students at KTH.

Replace the course list in [gpa.py](./gpa.py) with your own courses and run the script to calculate your GPA. A summary of your courses is also provided.

Example:
```sh
$ python3 gpa.py

Courses:
        Example 1      A   7.5 hp
        Example 3      A   7.5 hp
        Test course    A  10.5 hp
        course 2       B   3.0 hp
        Course 4       B  12.5 hp
        sample course  C   6.0 hp
        Course 1       D   4.5 hp
        Example 2      D   3.0 hp
        Course 3       F   3.0 hp

Summary:
        A: 3x,  B: 2x,  C: 1x,  D: 2x,  F: 1x

GPA: 4.30
```

The file [CDATE20_courses.py](./CDATE20_courses.py) contains a list of courses from the first three years of the CDATE20 program at KTH.

Notes:
- You should only add courses graded A-F, since courses graded as 'P' (Pass) are not taken into consideration when calculating GPA.
- If a partial grade of 'P' (Pass) is given for a non-completed course at KTH, the grade should be counted as a 3 (Insert 'E' to the course in the script).
