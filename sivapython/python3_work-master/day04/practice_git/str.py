course = 'Python for Beginners'

print(len(course))  # Outputs length of 'course' :: 20

print(course.upper())  # Outputs :: PYTHON FOR BEGINNERS

print(course.lower())  # Outputs :: python for beginners

print(course.title())  # Outputs :: Python For Beginners

print(course.find('P'))  # Outputs :: 1

print(course.find('o'))  # Outputs :: 4

print(course.find('z'))  # Outputs :: -1 because we don't have letter 'z' in the string

print(course.replace('Beginners', 'Absolute Beginners'))  # Outputs :: Python for Absolute Beginners

# Outputs :: Python for Beginners, replace is case sensitive. Needs exact word from the string
print(course.replace('beginners', 'Absolute Beginners'))

print(course.replace('P', 'J'))  # Outputs :: Jython for Beginners

print('Python' in course)  # Outputs :: True

print('python' in course)  # Outputs :: False. Needs exact word from string


