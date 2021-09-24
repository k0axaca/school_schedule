from school_schedule.student import Student
def test_grade_is_string():
    # Act
    student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

    # Assert
    assert type(student.grade) == str
    assert type(student.grade) != int

def test_grade_is_correct():
    # Act
    student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

    # Assert
    assert student.grade == "senior"
    
    