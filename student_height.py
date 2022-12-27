# # Run a program without using sum or len function method
student_height = input("Please enter the values: ").split()

for i in range(0, len(student_height)):
    student_height[i] = int(student_height[i])
print(student_height)

sum = 0
for i in student_height:
    sum = sum + i
print("The sum of the numbers are: ", sum)

number_of_student = 0
for i in student_height:
    number_of_student += 1
print("numbers of students are: ", number_of_student)

average = round(sum/number_of_student)
print("The average is: ", average)

# total_of_students = sum(student_height)
# count_of_students = len(student_height)
#
# average = total_of_students/count_of_students
# print(average)
# total = 0
#
# for i in range (1,101):
#     if i%2 == 0:
#         print(i)
#         total += i
# 
# print(total)