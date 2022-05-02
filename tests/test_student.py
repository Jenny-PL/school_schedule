from school_schedule.student import Student
from main import student_with_more_classes

def test_student_attributes_correctly_set():
    #arrange
    name = "Claire"
    year = "freshman"
    course_list = [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
    # act
    student = Student(name, year, course_list)
    # assert
    assert student.name == 'Claire'
    assert student.year == "freshman"
    assert student.course_list == [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
    
def test_alternate_student_attributes_correctly_set():
    #arrange
    # going to skip to make it simpler this time, and instead pass
    # values direcently into student instantiation

    # act
    student =  Student(
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
    # assert
    assert student.name == "Quinn"
    assert student.year == "junior"
    assert student.course_list == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
    
# test student_with_more_classes(student_a, student_b)
def test_student_with_more_classes_returns_correct_student():
    # arrange
    student_a = claire
    student_b = quinn
    # act
    result = student_with_more_classes(quinn, claire)
    # assert
    assert result == "Quinn"
