from src.addition import perform_operation

def perform_operation(multiplier, multiplicand):
    result = 0
    for _ in range(multiplier):
        result = perform_operation(result, multiplicand)
    return result