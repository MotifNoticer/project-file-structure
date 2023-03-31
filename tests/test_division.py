from src.division import perform_operation

def test_division():
    assert perform_operation(10, 5) == 2
    assert perform_operation(1, 1) == 1
    assert perform_operation(100, 2) == 50

