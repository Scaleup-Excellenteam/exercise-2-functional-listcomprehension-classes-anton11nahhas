import re


PARAGRAPH_TO_COUNT = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """


def count_words(text):
    """
    this function receives a string, uses a generator expression to remove the all special characters
    and store all the words in a list, then uses a dictionary comprehension to loop through that list
    and store the name and the length of each word and returns it to be printed, the program imports
    regular expression module to extract words only from the text.
    :param text: a string to operate on
    :return: a dictionary that has all the words from the text as keys and the values are the length of each word
    """
    clean = (word for word in re.split("\W+", text) if word.isalpha())
    result = {word.lower(): len(word) for word in clean}

    return result

def main():
    print(count_words(PARAGRAPH_TO_COUNT))


if __name__ == "__main__":
    main()
