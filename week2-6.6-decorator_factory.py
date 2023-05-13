from functools import wraps


class TypeCheckError(TypeError):
    """
    Custom error raised when an argument has an unexpected type.
    """

    def __init__(self, arg_name, expected_type):
        self.arg_name = arg_name
        self.expected_type = expected_type
        super().__init__(f"{arg_name} should be of type {expected_type.__name__}")


def type_check(correct_type):
    """
    this function is a decorator factory that checks if the type of argument given by user
    is the one we want, if not it raises a custom error message to indicate that the type
    added was wrong. if yes it returns the result to the wrapper, the wrapper returns it
    to the decorator and the function returns the decorator.
    :param correct_type: our correct type, in this case is INT
    :return: returns a decorator
    """

    def decorator(func):
        @wraps(func)
        def wrapper(arg, *args, **kwargs):
            if not isinstance(arg, correct_type):
                raise TypeCheckError(func.__name__, correct_type)
            return func(arg, *args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def times_2(num):
    """
    A function that takes an integer and returns its double value.
    :param num: variable that must be tested
    :return: the double of the input value
    """
    return num * 2


def main():
    print(times_2(5))  # output: success
    print(times_2("5"))  # output: exception


if __name__ == "__main__":
    main()
