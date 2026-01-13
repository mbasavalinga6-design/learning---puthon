# List comprehension
names = ["basava","shiva","darshan"]
upper_names = [name.upper() for name in names]

print(upper_names)

nums = [10, 15, 20, 25, 30]
even_nums = [n for n in nums if n % 2 == 0]

print(even_nums)

# dict comprehension
students = ["Ram", "Sita", "John"]
marks = [85, 90, 78]

student_marks = {students[i]: marks[i] for i in range(len(students))}

print(student_marks)
