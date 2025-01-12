def view_courses(courses_data: list[dict[str, str]]) -> None:
    """
    Displays a list of available courses with details such as course name, duration, 
    and instructor.

    Args:
        courses_data (list): A list of dictionaries containing course details. 
                              Each dictionary has keys like 'course_name', 'instructor', and 'duration'.
    """
    
    def view_courses(courses_data: list):
        print("\nAvailable Courses:")

        for i in range(len(courses_data)):
            print(f"{i + 1}, {courses_data[i]['course_name']} (Duration: {courses_data[i]['duration']}, Instructor: {courses_data[i]['instructor']})")