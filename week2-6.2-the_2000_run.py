import time


def timer(function, *args, **kwargs):
    """
    this function receives a pointer to another function and its params,
    the program imports time module so the function can compute the run
    time of that function, and returns it.
    :param function: this is a pointer to function
    :return: the time taken to undergo the function
    """

    start = time.perf_counter()
    function(*args, **kwargs)
    end = time.perf_counter()

    return end - start


def main():
    result = timer(print, "Hello")
    print(result)


if __name__ == "__main__":
    main()
