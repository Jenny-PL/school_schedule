# stopped lesson at 33mins.
# https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=6269b2ce-078b-4b7a-b915-ae6a0133fe8f
class Student:
    def __init__(self, name, year, course_list):
        self.name = name
        self.year = year
        self.course_list = course_list
        # self.course_list = course_list.copy()    #shallow copy
        # self.course_list = course_list[:]     #shallow copy
        #self.course_list = copy.deepcopy  # if use import copy 

    def add_class(self, course):
        # self.course_list += [course]
        self.course_list.append(course)

    def get_num_classes(self):
        # make a set of courses, to ensure no duplicates being counted
        course_set = set(self.course_list)
        return len(course_set)

    def summary(self):
        # To wrap the line: use () outside of entire string; use " to end on line
        # add in f-string to start next wrapped- line.
        return (f"{self.name} is signed up for {self.get_num_classes()} classes. "
            f"Here is a list of the courses: {', '.join(self.course_list)}.  "\
                f"{self.name} is a {self.year} this year.")

        # Another line-wrap option:  End ", use \, and start new f-string:
        return f"{self.name} is signed up for {self.get_num_classes()} classes. "\
            f"Here is a list of the courses: {self.course_list}"
    
