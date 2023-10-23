courses = ["MIT", "CyberSecurity", "Datascience"]
print(courses)
# Accessing an element in an Array
print(courses[1])
# looping through the array
for course in courses:
    print(course)

# Adding an element in an Array
courses.append("Android Development")
print(courses)

# removing an element in array
courses.remove("MIT")

print(courses)