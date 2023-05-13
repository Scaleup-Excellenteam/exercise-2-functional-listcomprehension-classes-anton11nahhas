TEST_DICT = ["hi", "bye", "yo", "try"]


def group_by(function, iterable_object):
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
    result = {key: [word for word in iterable_object if function(word.strip()) == key] for key in
              set(map(function, iterable_object))}
    return result


def main():
    print(group_by(len, TEST_DICT))


if __name__ == "__main__":
    main()
