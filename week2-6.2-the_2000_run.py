import time


def timer(f, *args, **kwargs):
    """
    this function receives a pointer to another function and its params,
    the program imports time module so the function can compute the run
    time of that function, and returns it.
    :param f: this is a pointer to function
    :param p: multiple parameters
    :return: the time taken to undergo the function
    """

    start = time.time()
    f(*args, **kwargs)
    end = time.time()
    return end - start


print(timer(print, "Hello"))
