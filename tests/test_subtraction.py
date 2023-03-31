from src.subtraction import perform_operation

def test_subtraction():
    # Assert
    assert perform_operation(1, 1) == 0
    assert perform_operation(100, 1) == 99
    assert perform_operation(99, 55) == 44