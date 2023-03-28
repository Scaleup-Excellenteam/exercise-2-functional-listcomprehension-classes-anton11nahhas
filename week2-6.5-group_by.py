def group_by(func, it):
    """
    this function receives a function and an iterable function, the function uses
    a dict comprehension that consists of a list comprehension to return a dict
    which its keys are the value of that function for each iterable object,
    and the value is all the iterable objects that satisfies that function
    :param func: a function
    :param it: an iterable object
    :return: a dict, keys are the values of that function and the values are the iterable members that
            satisfy that function
    """
    result = {func(word.strip()): [w for w in it if func(w) == func(word)] for word in it}
    return result


print(group_by(len, ["hi", "bye", "yo", "try"]))
