import src.addition as addition

def test_addition():
    # Assert
    assert perform_operation(1, 1) == 2
    assert perform_operation(800, 88) == 888
    assert perform_operation(-1, 1) == 0