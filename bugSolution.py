def function_with_uncommon_error(x):
    try:
        result = 1 / x
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None  #Explicitly return a value
    except TypeError:
        print("Cannot divide by a non-numeric type!")
        return None #Explicitly return a value
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None #Explicitly return a value
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

# Example that will hit the generic exception
print(function_with_uncommon_error([1,2]))