#1 create empty dictonary
#2. promt user for student name, add value to dictonary
#3. promt user for student age
#4. promt user for student grade
#5. use a loop prompt the user for the studens hobbies until they enter done
#6. print the dictonary to the console

# 1. Create empty dictionary
student = {}

# 2. Prompt user for student name, add to dictionary
student_name = input("Enter the student's name: ")
student["Name"] = student_name

# 3. Prompt user for student age
student_age = input("Enter the student's age: ")
student["Age"] = student_age

# 4. Prompt user for student grade
student_grade = input("Enter the student's grade: ")
student["Grade"] = student_grade

# 5. Use a loop to prompt the user for hobbies until they enter "done"
hobbies = []
print("Enter the student's hobbies one by one. Type 'done' when finished.")
while True:
    hobby = input("Enter a hobby: ")
    if hobby.lower() == "done":
        break
    hobbies.append(hobby)

student["Hobbies"] = hobbies

# 6. Print the dictionary to the console
print("\nStudent Information:")
print(student)


