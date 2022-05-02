from school_schedule.student import Student

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

print(quinn.name)
quinn.add_class("Painting")
print(len(quinn.course_list))
print(quinn.course_list)
print(quinn.get_num_classes())
print(quinn.summary())

# second instance
claire = Student(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )
claire.get_num_classes()
print(claire.summary())

# Extra:
# - create a function that will return the student with more classes
def student_with_more_classes(student_a, student_b):
    if student_a.get_num_classes() > student_b.get_num_classes():
        return student_a.name
    elif student_a.get_num_classes() > student_b.get_num_classes():
        return f"They are taking equal number of classes: {student_a.get_num_classes()} each."
    else:
        return student_b.name

print(student_with_more_classes(quinn, claire))

# - create a test for that function
