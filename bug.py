def function_with_uncommon_error(x):
    try:
        result = 1 / x
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Cannot divide by a non-numeric type!")
    else:
        return result
    finally:
        print("This always runs!")

# Example of a common usage
print(function_with_uncommon_error(2))

# Example that will hit the TypeError
print(function_with_uncommon_error("a"))

# Example that will hit the ZeroDivisionError
print(function_with_uncommon_error(0))