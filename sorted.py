def is_sorted(list):
    """

    :param List:
    :return: True if list is sorted
    >>> unsorted_list = [5, 3, 2]
    >>> sorted_list = [1, 2, 3]
    >>> empty_list = []
    >>> is_sorted(unsorted_list)
    False
    >>> is_sorted(sorted_list)
    True
    >>> is_sorted(empty_list)
    False
    """
    index = 0
    if list == [None]:
        return False
    while index <= len(list) - 2:
        if list[index] > list[index + 1]:
            sorted_check = False
            break
        else:
            sorted_check = True
            index += 1

    return sorted_check


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
