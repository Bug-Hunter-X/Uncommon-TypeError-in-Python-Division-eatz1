def improved_function_with_error_handling(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int, float)):
            raise TypeError("Both inputs must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e) 

# Example usage
print(improved_function_with_error_handling(10, 2))  # Output: 5.0
print(improved_function_with_error_handling(10, 0))  # Output: Division by zero
print(improved_function_with_error_handling(10, "hello"))  # Output: Both inputs must be numbers
print(improved_function_with_error_handling([1,2], 2)) # Output: Both inputs must be numbers