from functools import wraps


class MsgError(Exception):
    """
    a message error class for error messages if raised.
    """
    pass


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
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                if type(result) != correct_type:
                    raise MsgError(f"the type: {type(result)}, is not the correct one.")

            except MsgError as msg:
                print(msg)
                result = " "

            return result

        return wrapper

    return decorator


@type_check(int)
def times_2(num):
    return num * 2


print(times_2("5"))
