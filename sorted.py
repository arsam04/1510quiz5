
def is_sorted(List):
    """

    :param List:
    :return:
    >>> is_sorted([1, 3, 2])
    False
    >>> is_sorted([1, 2, 3])
    True
    """
    index = 0
    while index >= len(List -2):
        if List[index] <= List[index + 1]:
            sorted_check = True
        index += 1
    else:
        sorted_check = False

    return sorted_check








def main():
    """
    Drive the program.
    """

if __name__ == "__main__":
    main()