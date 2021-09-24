from school_schedule.student import Student

def test_student_class_name_is_correct():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  # assert
  assert student.name == "Trenisha"

def test_class_name_in_add_class_is_string():
    # arrange
    class_name = "Biology"
    student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

    #act
    one_class = student.add_class(class_name)

    # assert
    assert type(class_name) == str
    assert type(class_name) != int

