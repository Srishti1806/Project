from student import calculate_average, assign_grade


def test_average():
    assert calculate_average(90, 80, 70) == 80.0


def test_grade():
    assert assign_grade(95) == "S"
    assert assign_grade(85) == "A"
    assert assign_grade(70) == "B"
    assert assign_grade(55) == "C"
    assert assign_grade(45) == "D"
    assert assign_grade(30) == "F"
